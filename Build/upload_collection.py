import sys

import requests
import getpass
import json

API_URL = "https://readers.kontinua.org/api/"
NUMBER_OF_WORKBOOKS = 36


# Some utility functions for nice outputs.
def print_pretty_json(json_obj: dict):
    try:
        if isinstance(json_obj, str):  # If it's a string, try to parse it as JSON
            json_obj = json.loads(json_obj)
        print(json.dumps(json_obj, indent=4))
    except json.JSONDecodeError:
        print("Could not decode JSON properly. Raw output:")
        print(json_obj)


def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


# CLI functions.
def get_auth_token() -> str | None:
    '''
    Authenticaes the user and returns the token
    Prints any failure messages, and returns none if it fails for any reason.
    '''
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    body = {
        "username": username,
        "password": password
    }

    response = requests.post(API_URL + "token/", json=body)

    if response.status_code == 200:
        token = response.json()["token"]
        print(f"Welcome {username}!")
        return token
    else:
        print(f"Failed to authenticate: {response.status_code} != 200")
        print_pretty_json(response.json())
        return None


def retrieve_latest_collection(localization: str, token: str) -> dict | None:
    '''
    Retrieves the latest collection for a given localization
    '''
    response = requests.get(API_URL + "collections/", params={"localization": localization},
                            headers={"Authorization": f"Token {token}"})

    if not response.status_code == 200:
        print(f"Failed to retrieve latest collection: {response.status_code} != 200")
        print_pretty_json(response.json())
        return None

    if len(response.json()) == 0:
        return {}

    # We expect the backend to return the collections in sorted order.
    return response.json()[0]


def create_new_collection(localization: str, major_version: int, minor_version: int, token: str) -> dict | None:
    '''
    Creates a new collection with the given parameters
    '''
    body = {
        "localization": localization,
        "major_version": major_version,
        "minor_version": minor_version
    }

    response = requests.post(API_URL + "collections/", json=body, headers={"Authorization": f"Token {token}"})

    if not response.status_code == 201:
        print(f"Failed to create new collection: {response.status_code} != 201")
        print_pretty_json(response.json())
        return None

    return response.json()


def create_workbook(collection: dict, workbook_number: int, token: str) -> dict | None:
    # This assumes workbooks are numbered 1 -> 99
    workbook_number = str(workbook_number).zfill(2)

    localization_file_path = collection["localization"].replace("-", "_")

    chapter_meta_path = f"./Resources-{localization_file_path}/workbook-{workbook_number}.json"
    pdf_file_path = f"./Workbooks-{localization_file_path}-Letter/workbook-{workbook_number}.pdf"

    with open(chapter_meta_path, "r") as chapter_meta, \
            open(pdf_file_path, "rb") as pdf_file:

        body = {
            "number": workbook_number,
            "collection": collection["id"],
            "chapters": chapter_meta.read()
        }

        files = {
            "pdf": (
                f"workbook-{workbook_number}-{collection["localization"]}-{collection["major_version"]}.{collection["minor_version"]}.pdf",
                pdf_file, "application/pdf")
        }

        headers = {
            "Authorization": f"Token {token}"
        }

        response = requests.post(API_URL + "workbooks/", data=body, files=files, headers=headers)

        if response.status_code != 201:
            print(f"Failed to create new workbook: {response.status_code} != 201")

            print("Response Dump:")
            response_data = response.json()
            print_pretty_json(response_data)

            if "chapters" in response_data:
                print("Json Schema Validation Errors:")
                for error in response_data["chapters"]:
                    print(error)

            return None

        return response.json()


def release_collection(collection: dict, token: str) -> dict | None:
    response = requests.patch(API_URL + f"collections/{collection["id"]}/release/",
                              headers={"Authorization": f"Token {token}"})

    if response.status_code != 200:
        print(f"Failed to release collection: {response.status_code} != 200")
        print_pretty_json(response.json())
        return None

    return response.json()


def main():
    token = get_auth_token()

    if token is None:
        return

    print("Using address: ", API_URL)

    localization = input("Localization (i.e. en-US): ")

    collection = retrieve_latest_collection(localization, token)

    if collection is None:
        return

    if collection == {}:
        print("There are no collections for this localization yet!")
    else:
        print("Latest version for localization: ", f"{collection['major_version']}.{collection['minor_version']}")

    print("Enter new major and minor version numbers for the new collection:")
    major_version = int(input("Major version: "))
    minor_version = int(input("Minor version: "))

    new_collection = create_new_collection(localization, major_version, minor_version, token)

    if not new_collection:
        return

    collection_name = f"{new_collection['localization']} v{new_collection['major_version']}.{new_collection['minor_version']}"
    print(
        f"Going to add {NUMBER_OF_WORKBOOKS} workbooks to collection:\n{collection_name}")
    input("Press Enter to continue (ctrl-C to cancel)...")

    progress_bar(0, NUMBER_OF_WORKBOOKS)
    for i in range(1, NUMBER_OF_WORKBOOKS + 1):
        workbook = create_workbook(new_collection, i, token)
        if workbook is None:
            print(f"Failed to create workbook {i}. Cancelling collection creation.")
            print(f"Note, you will need to delete collection manually.")
        progress_bar(i, NUMBER_OF_WORKBOOKS)

    print("\nDone!")
    print("Want to release this collection now?")
    yes_or_no = input("Enter 'yes' to release, 'no' to cancel: ")

    if yes_or_no.lower() == "yes":
        release_collection(new_collection, token)
        print(f"{collection_name} released!")
    else:
        print("Collection not released.")


if __name__ == "__main__":
    main()

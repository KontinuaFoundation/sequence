from email.policy import default
import json
import os
import readline
from tkinter import NO

filename = "digital_resources.json"

top_level = ["files", "requires", "covers"]
top_level_prompts = {"files":"Downloads", "requires":"Prerequisite modules", "covers":"Covered learning objectives"}

structures = {"files":["path","desc"],
              "covers":["id", "desc", "videos", "references"]}

prompts = {("files","desc"):"Description of download file", 
           ("files","path"):"Path to download file (relative to CWD)",

           ("requires"):"Prerequisite module identifiers, comma-separated",
           ("covers","id"): "Objective module identifier", 
           ("covers","desc"):"Objective module description",
           ("covers","videos"):"Objective module video URLs, comma-separated",
           ("covers","references"):"Objective module reference URLs, comma-separated"}

types = {("files","desc"):"string", 
           ("files","path"):"string",
           ("requires"):"stringlist",
           ("covers","id"): "string", 
           ("covers","desc"):"string",
           ("covers","videos"):"stringlist",
           ("covers","references"):"stringlist"}

# Get a single string with a default value
def inputWithReplacement(prompt,i=0, default_value=None):
    fprompt = prompt
    if i > 0:
        fprompt = f"{fprompt} {i}:"
    else:
        fprompt = f"    {fprompt}: "

    if default_value is not None:
        def hook():
            readline.insert_text(default_value)
            readline.redisplay()

        readline.set_pre_input_hook(hook)

    result = input(fprompt).strip()
    readline.set_pre_input_hook()
     
    return result
    
# Get a list of strings (user comma-separates)
def inputListStringWithReplacement(prompt, i=0, default_value=None):
    if default_value is None:
        defstring = None
    else:
        defstring = ",".join(default_value)

    stringresult = inputWithReplacement(prompt, i, defstring)
    if len(stringresult) > 1:
        return [s.strip() for s in stringresult.split(",")]
    else:
        return []

# Call the right input method based on dtype
def inputWithType(dtype, prompt, i=0, default_value=None):
    if dtype=="stringlist":
        return inputListStringWithReplacement(prompt, i, default_value)
    else:
        return inputWithReplacement(prompt, i, default_value)

# What the value in the old dictionary?
def defvalue(ddict, topkey, childkey, i):
    if topkey not in ddict:
        return None
    category = ddict[topkey]

    if len(category) <= i:
        return None

    idict = category[i]

    if childkey not in idict:
        return None
    
    return idict[childkey]
    

# If the file already exists, read it
if os.path.exists(filename):
    with open(filename, "r") as f:
        original_data_dict = json.load(f)
        print(f"Loaded:\n{json.dumps(original_data_dict, indent=2)}\n")
else: # Else create a new one
    original_data_dict = {}

# Get the topic index
with open("../../topic_index.json", "r") as f:
    topics = json.load(f)

# Make a dictionary that we can edit
data_dict = {}

# Walk the top-level keys
for tkey in top_level:
    tprompt = top_level_prompts[tkey]
    print(f"*** {tprompt} ***")
    # No children? Just a single entry
    if tkey not in structures:
        base_prompt = prompts[(tkey)]
        dtype = types[(tkey)]
        if tkey in original_data_dict:
            old_value = original_data_dict[tkey]
        else:
            old_value = None
        confirmed = False
        while not confirmed:
            new_value = inputWithType(dtype, base_prompt, 0, old_value)

            if tkey=="requires" and len(new_value) > 0:
                for k in new_value:
                    if k in topics:
                        d = topics[k]
                        print(f'{k}: \"{d["desc"]}\"')
                    else:
                        print(f'{k} is unknown!')
                confirm = inputWithReplacement("Confirmation", default_value="y")
                if confirm.startswith("y"):
                    confirmed = True
                else:
                    confirmed = False

            else:
                confirmed = True
        data_dict[tkey] = new_value

    # Children? Gather answer as a list of dicts
    else:

        # What are the keys for each dictionary?
        children = structures[tkey]

        entry_index = 0
        stop = False
        new_list = []
        while not stop:
    
            new_dict = {}
            for (j, child) in enumerate(children):
                base_prompt = prompts[(tkey, child)]
                dtype = types[(tkey, child)]
                old_value = defvalue(original_data_dict, tkey, child, entry_index)
                new_value = inputWithType(dtype, base_prompt, entry_index + 1, old_value)

                # Was nothing entered?
                if new_value is None or len(new_value) == 0:
                    # Was this the first dictionary key?
                    if j == 0:
                        # Move to the next top level key
                        stop = True
                        break
                else:
                    new_dict[child] = new_value
            # Have we gone through all the keys?
            if len(new_dict) > 0:

                # Add the dict to the list
                new_list.append(new_dict)

            # Go to the next dictionary 
            entry_index += 1

        # Add the list to the output    
        data_dict[tkey] = new_list

outstr = json.dumps(data_dict, indent=2)
print(f"Preparing to fill {filename} with \n{outstr}\n")
confirmation = input("Type 'y' to confirm:")

# Save the work somewhere...
if confirmation != 'y':
    filename = "notconfirmed.json"

with open(filename, "w") as f:
    f.write(outstr)
    print(f"Wrote {filename}")       


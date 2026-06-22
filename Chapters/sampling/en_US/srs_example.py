import pandas as pd  # import the pandas library for working with tabular data

# Load data from a local CSV file
df = pd.read_csv("srs_example.csv")  # read the CSV into a DataFrame

# Choose one year and keep only the country name and population Population
year = 2022  # set the year to filter by
df_year = df[df["Year"] == year][["Country Name", "Population"]].reset_index(drop=True)  # filter rows to year 2022, keep only two columns, then reset the row index

# Take a simple random sample of 5 countries
# (No random_state means different countries each time, showing sampling variability)
sample_size = 5  # number of countries to sample
sample = df_year.sample(n=sample_size)  # randomly select 5 rows from the filtered data

print(f"Simple random sample of {sample_size} countries in {year}:")  # print a message describing the sample
print(sample[["Country Name", "Population"]].to_string(index=False))  # print the sampled countries and populations without the DataFrame index

print(f"\nTotal countries in {year}: {len(df_year)}")  # print how many countries were available for that year
print("\nIn simple random sampling, every country has the same chance of being selected.")  # print a short explanation of simple random sampling


import pandas as pd

# Load data from a local CSV file
df = pd.read_csv("srs_example.csv")

# Choose one year and keep only the country name and population value
year = 2022
df_year = df[df["Year"] == year][["Country Name", "Value"]].reset_index(drop=True)

# Take a simple random sample of 5 countries
# (No random_state means different countries each time, showing sampling variability)
sample_size = 5
sample = df_year.sample(n=sample_size)

print(f"Simple random sample of {sample_size} countries in {year}:")
print(sample[["Country Name", "Value"]].to_string(index=False))

print(f"\nTotal countries in {year}: {len(df_year)}")
print("\nIn simple random sampling, every country has the same chance of being selected.")


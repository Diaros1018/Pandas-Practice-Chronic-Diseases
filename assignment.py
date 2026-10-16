import pandas as pd

us_chronic_disease_file = './US_chronic_diseases.csv'
df = pd.read_csv(us_chronic_disease_file, low_memory=False)


def get_melanoma_mortality_information_by_state(state_code):
    filtered_df = df[
        (df["LocationAbbr"] == state_code.upper()) &
        (df["Question"] == "Melanoma, mortality")
    ]

    average = filtered_df["DataValueAlt"].mean()
    return round(average, 2)


def get_asthma_mortality_information_by_state(state_Code):
    filtered_df = df[
        (df["LocationAbbr"] == state_Code.upper()) &
        (df["Question"] == "Asthma mortality rate")
    ]

    average = filtered_df["DataValueAlt"].mean()
    return round(average, 2)


def get_chronic_liver_mortality_by_state(state_code):
    filtered_df = df[
        (df["LocationAbbr"] == state_code.upper()) &
        (df["Question"] == "Chronic liver disease mortality") &
        (df["DataValueType"] == "Crude Rate")
    ]

    average = filtered_df["DataValueAlt"].mean()
    return round(average, 2)


def get_missing_values_count_by_state(state_code):
    filtered_df = df[
        df["LocationAbbr"] == state_code.upper()
    ]

    return int(filtered_df["DataValueAlt"].isnull().sum())


if __name__ == "__main__":
    print("Melanoma TX:",
          get_melanoma_mortality_information_by_state("tx"))

    print("Asthma TX:",
          get_asthma_mortality_information_by_state("tx"))

    print("Chronic Liver TX:",
          get_chronic_liver_mortality_by_state("tx"))

    print("Missing Values TX:",
          get_missing_values_count_by_state("tx"))
    print(df[df["Question"].str.contains("Melanoma", case=False, na=False)]["Question"].unique())
    
states = ['tx', 'va', 'ga', 'fl', 'ca',
          'il', 'ny', 'nj', 'tn', 'co']

expected_melanoma = [80.72, 47.4, 47.22, 123.19, 131.95,
                     74.7, 66.25, 42.45, 45.93, 33.44]

expected_asthma = [41.31, 26.01, 27.08, 37.53, 64.92,
                   43.81, 57.5, 29.81, 22.42, 18.55]

expected_liver = [11.74, 9.72, 9.08, 12.42, 15.3,
                  9.52, 7.45, 8.39, 13.57, 18.93]

expected_missing = [4628, 5846, 5468, 4195, 4599,
                    8349, 4478, 5383, 7502, 5423]

passed = 0

for i, state in enumerate(states):
    results = [
        get_melanoma_mortality_information_by_state(state),
        get_asthma_mortality_information_by_state(state),
        get_chronic_liver_mortality_by_state(state),
        get_missing_values_count_by_state(state)
    ]

    expected = [
        expected_melanoma[i],
        expected_asthma[i],
        expected_liver[i],
        expected_missing[i]
    ]

    for result, correct in zip(results, expected):
        if result == correct:
            passed += 1
        else:
            print(f"ERROR in {state}: {result} != {correct}")

print(f"Tests passed: {passed}/40")


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

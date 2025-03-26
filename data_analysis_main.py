def create_dirs():
    import os

    result_dir = 'csv_results/class_proportions'
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)


if __name__ == "__main__":
    import pandas as pd
    from src.categorical_utilities import categorical_summary
    from src.numerical_utilities import statistics_summary

    # I got all the information about the data in the Jupyter Notebook,
    # thus here I don't really analyse it anymore, just process.

    # Load the dataset
    df = pd.read_csv('data/billionaires_statistics_dataset.csv')

    # Drop the tables I won't use (unusable due to huge amount of null values)
    df.drop(['title', 'state', 'residenceStateRegion', 'organization'], axis=1, inplace=True)

    # Change GDP to a numerical series to facilitate numerical analysis later on
    df['gdp_country'] = df['gdp_country'].replace('[$,]', '', regex=True).astype(float)

    numerical_series = ['rank', 'finalWorth', 'age', 'gdp_country', 'birthYear', 'cpi_country', 'cpi_change_country',
                        'gross_primary_education_enrollment_country', 'gross_tertiary_education_enrollment',
                        'life_expectancy_country', 'tax_revenue_country_country', 'total_tax_rate_country',
                        'population_country', 'latitude_country', 'longitude_country']

    categorical_series = ['category', 'personName', 'country', 'city', 'source', 'industries', 'industries', 'countryOfCitizenship',
                         'selfMade', 'status', 'gender', 'lastName', 'firstName']

    create_dirs()

    statistics_summary(df, numerical_series)
    categorical_summary(df, categorical_series)
import pandas as pd

nyt_county = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
nyt_state = 'https://github.com/nytimes/covid-19-data/blob/master/us-states.csv'
# usa_facts = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv'
# mt_data = 'https://www.arcgis.com/sharing/rest/content/items/0d47920e54e0420cb604213acc8761d5/data'
# nls_mt_data = './mt_coronavirus_status.csv'

print('imported covid_data.py')

def read_county_data_from_web():
	datatypes = {
        'date': 'str',
        'county': 'str',
        'state': 'str',
        'fips': 'Int64',
        'cases': 'Int64',
        'deaths': 'Int64'
	}
	counties_df = pd.read_csv(nyt_county, dtype=datatypes, parse_dates=[0])
	
	counties_df.set_index('date',  inplace=True)
	counties_df.fillna(0)
	return counties_df
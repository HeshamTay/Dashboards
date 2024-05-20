import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://github.com/HeshamTay/Dashboards/raw/main/preprocessed_data.csv')
st.set_page_config(page_title='Prosperity Measures', page_icon=':earth_africa:',layout='wide')
st.title(" :earth_africa: Prosperity Measures")

years = list(range(2001, 2020))
selected_year = st.selectbox('Select a Year', years)

measurements = [i for i in df.columns.tolist() if i not in ['Year', 'Country Name', 'Country Code', 'Region', 'IncomeGroup']]
selected_measurement = st.multiselect('Select the measurement you want to be visualized',measurements, max_selections=1)
# Get the unique regions
regions = df['Region'].unique().tolist()

# Let the user select the region
selected_region = st.multiselect('Select a Region', regions)

# Filter the DataFrame based on the user's region selection
filtered_df = df[df['Region'].isin(selected_region)]

# Get the unique countries in the selected regions
countries = filtered_df['Country Name'].unique().tolist()

# Country Selection
selected_countries = st.multiselect('Select Countries', countries)

# Filter the DataFrame
filtered_df = filtered_df[filtered_df['Country Name'].isin(selected_countries)]

final_df = filtered_df[filtered_df['Year'] == selected_year]

if selected_measurement:
   fig = px.bar(final_df, x='Country Name', y=selected_measurement[0], height=700, width=700)
   st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Please select at least one measurement.")

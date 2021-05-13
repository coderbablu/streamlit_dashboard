import streamlit as st
from streamlit_folium import folium_static
import folium

from PIL import Image


# define your app content
def main():
    # Use the full page instead of a narrow central column
    st.set_page_config(layout="wide")

    # colimg1, colimg2 = st.beta_columns(2)
    # with colimg1:
    # image1 = Image.open('Trillion_Fund_Logo.jpg')
    # st.image(image1, width=None)

    # with colimg2:
    # image2 = Image.open('Omdena_Logo.jpg')
    # st.image(image2, width=None)

    st.title("Trillion Tree Fund")

    st.header("Input Details")

    colA1, colA2, colA3 = st.beta_columns(3)
    with colA1:
        st.info("Amount of Investment")
        amount_investment = st.number_input("USD", value=50000000, step=1000000)

        st.info("Type of Tree Species")
        trees1 = st.text_input(" ")
        trees2 = st.text_input("  ")
        trees3 = st.text_input("   ")
        trees4 = st.text_input("    ")

    with colA2:
        colA2.info("Project Location")
        latitude = st.text_input("Latitude / Longitude")

        st.info("Number of Trees")
        trees1_amount = st.number_input(" ", value=1000, step=100)
        trees2_amount = st.number_input("  ", value=1000, step=100)
        trees3_amount = st.number_input("   ", value=1000, step=100)
        trees4_amount = st.number_input("    ", value=1000, step=100)

    with colA3:
        hide_map = st.checkbox("Check box to hide the map")
        if not hide_map:
            m = folium.Map()
            m.add_child(folium.LatLngPopup())
            folium_static(m)

    st.markdown(" ")

    st.header("Asset Details")

    colC1, colC2, colC3, colC4 = st.beta_columns(4)
    with colC1:
        st.info("Physical Risk(s) Location(s)")
    with colC2:
        loc_invest_asset1 = st.text_input("Investor's Assets 1")
        loc_invest_asset2 = st.text_input("Investor's Assets 2")
        loc_invest_asset3 = st.text_input("Investor's Assets 3")

    with colC3:
        loc_client_asset1 = st.text_input("Client Assets 1")
        loc_client_asset2 = st.text_input("Client Assets 2")
        loc_client_asset3 = st.text_input("Client Assets 3")

    with colC4:
        loc_supplier_asset1 = st.text_input("Supplier Assets 1")
        loc_supplier_asset2 = st.text_input("Supplier Assets 2")
        loc_supplier_asset3 = st.text_input("Supplier Assets 3")

    colB1, colB2, colB3, colB4 = st.beta_columns(4)
    colB1.info("Type(s) of Tangible Asset(s)")
    colB2.selectbox('Choose one of the below',
                    ['Buildings', 'Manufacturing Facility ', 'Agricultural'])

    # Code from Komal

    st.header("Owned Asset Details")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.info("Type of Asset for Rent")
        asset_for_rent = st.multiselect('Select the Assets', ['Land', 'Building', 'Machinery', 'Other Asset'],
                                        key='rent')

        st.info("Value of Assets for Rent")
        asset1 = st.number_input("For Asset 1 (in USD)", value=0, step=100, key='asset1')
        asset2 = st.number_input("For Asset 2 (in USD)", value=0, step=100, key='asset2')
        asset3 = st.number_input("For Asset 3 (in USD)", value=0, step=100, key='asset3')

    with col2:
        st.info("Type of Asset for Sale")
        asset_for_sale = st.multiselect('Select the Assets', ['Land', 'Building', 'Machinery', 'Other Asset'],
                                        key='sale')
        st.info("Value of Assets for Sale")
        asset11 = st.number_input("For Asset 1 (in USD)", value=0, step=100, key='asset11')
        asset22 = st.number_input("For Asset 2 (in USD)", value=0, step=100, key='asset22')
        asset33 = st.number_input("For Asset 3 (in USD)", value=0, step=100, key='asset33')

    with col3:
        st.info("Annual Utility Costs (per asset)")
        a1 = st.number_input("For Land (in USD)", value=0, step=100, key='a1')
        a2 = st.number_input("For Building (in USD)", value=0, step=100, key='a2')
        a3 = st.number_input("For machinery (in USD)", value=0, step=100, key='a3')
        a4 = st.number_input("Other Asset(in USD)", value=0, step=100, key='a4')

    st.markdown(" ")

    st.header("Other Information")

    col11, col12, col13 = st.beta_columns(3)
    col11.info("Other Information")
    Carbon_Emission = col12.number_input("Total Annual Carbon Emissions (tons)", value=0)
    Annual_Tax_Benefits = col13.number_input("Annual Tax Benefits Received for FLR (USD)", value=0, step=100)

    # Code from Bandhav
    # For Banks/Lenders Only - Bandhav
    st.header('For Banks/Lenders only')
    cola2, cola3 = st.beta_columns(2)
    # with cola1:
    # st.info('Amount of credit risk due to climate risk affected areas')
    with cola2:
        # st.info('Credit risk amount (USD)')
        credit_amount = st.number_input('Credit risk amount (USD)', value=1000000, step=1000)
    with cola3:
        # st.info('Type of climate risk')
        climate_risk_banks = st.selectbox('Type of climate risk',
                                          ['Tropical Cyclone', 'Drought', 'Flood', 'Wildfire', 'Sea Level Rise'])

    # For Insurers Only (Public & Private Sector) - Bandhav
    st.header('For Insurers only (Public & Private Sector)')
    colb1, colb2, colb3 = st.beta_columns(3)
    with colb1:
        climate_risk_insurers = st.selectbox('Type of climate risks',
                                             ['Tropical Cyclone', 'Drought', 'Flood', 'Wildfire', 'Sea Level Rise'])
    with colb2:
        modelling_loss_insurers = st.number_input('Catastrophe modelling expected loss (USD)', value=0)
    with colb3:
        job_loss_insurers = st.number_input('Avg no of job losses due to natural disasters', value=0)

    # For Hospital/Hotel Owners Only - Bandhav
    st.header('For Hospital/Hotel Owners only')
    colc1, colc2, colc3 = st.beta_columns(3)
    with colc1:
        avg_room_rate_hotel = st.number_input('Average Room Rate (USD)', value=500)
        ann_touri_rev_hotel = st.number_input('Annual Tourism Revenue (Past 3 Years)', value=500)
    with colc2:
        avg_rate_view_hotel = st.number_input('Average Room Rate with View (USD)', value=500)
        ann_touri_arr_hotel = st.number_input('Annual no of Tourist Arrivals (Past 3 Years)', value=500)
    with colc3:
        avr_rate_no_view_hotel = st.number_input('Average Room Rate, No View (USD)', value=500)
        rev_loss_natudis_hotel = st.number_input('Revenue Losses due to Natural Disasters', value=500)

    # For Public Investors - Bandhav
    st.header('For Public Investors')
    cold1, cold2, cold3 = st.beta_columns(3)
    with cold1:
        st.text('')
        st.info('Health Related')
    with cold2:
        ann_comdis_public = st.number_input('Total Annual Expenditure on Noncommunicable Diseases (USD)', value=500)
        ann_prolos_public = st.number_input('Total Annual National Health Related Productivity Loss (USD)', value=500)
    with cold3:
        ann_resdis_public = st.number_input('Total Annual Expenditure on Respiratory Diseases (USD)', value=500)

    cole1, cole2, cole3 = st.beta_columns(3)
    with cole1:
        st.text('')
        st.info('Tourism Related')
    with cole2:
        ann_tour_public = st.number_input('Annual Tourism Revenues (Past 3 Years) (USD)', value=500)
        cur_tousiz_public = st.number_input('Current Tourism Sector Size (USD)', value=500)
    with cole3:
        ann_inttou_public = st.number_input('Annual no of Internationall Tourist Arrivals (Past 3 Years)', value=500)
        tour_gdp_public = st.number_input('Tourism Sector as % of GDP (USD)', value=500)

    colf1, colf2, colf3 = st.beta_columns(3)
    with colf1:
        st.text('')
        st.info('Jobs Related')
    with colf2:
        tot_jobs_public = st.number_input('Total no of Jobs In Forestry and Ecotourism Sectors', value=0)
        labor_prod_public = st.number_input('National Labor Productivity (GDP per hour worked)', value=0)
    with colf3:
        avg_joblos_public = st.number_input('Average no of Job Losses Due to Natural Disasters', value=0)
        tot_incjob_public = st.number_input('Total Earned Income from Jobs in Forestry, Ecotourism (USD)', value=500)

    colh1, colh2, colh3 = st.beta_columns(3)
    with colh1:
        st.text('')
        st.info('Total Annual Number of Deaths')
    with colh2:
        noofdeath_disease = st.number_input('Attributable to NCDs, Respiratory Diseases, Pollution, Mental Health',
                                            value=0)
    with colh3:
        noofdeath_hygiene = st.number_input('Attributable to Unsafe Water, Sanitation, Hygeine (per capita)', value=0)

    colg1, colg2, colg3 = st.beta_columns(3)
    with colg1:
        st.text('')
        st.info('Others')
    with colg2:
        ann_foss_public = st.number_input('Total Annual Fossil Fuel Subsidies (USD)', value=500)
        avg_life_public = st.number_input('Average Life Expectancy', value=0)
    with colg3:
        ann_acaavg_public = st.number_input('Annual Academic Average', value=0)


# execute the main function
if __name__ == '__main__':
    main()
#Lets start with importing the whole data frame from the annual emissions csv
#then lets make a function which manipulates it to only give the data we want
import pandas as pd


class Emissions(object):

    def __init__(self, name):
        self.name = name
        #Might want to use different data sources here.
        #so lets call the data frames something that makes clear their origin
        if 'self.df_edgar_co2_kt' not in locals():
            print("Reading URL again")
            url_edgar_co2= 'http://edgar.jrc.ec.europa.eu/booklet2017/EDGARv432_FT2016_CO2_total_emissions_1970-2016.csv'
            #Numbers in this sheet only include CO2 emissions
            #They are in ktonnes of CO2 per year
            self.df_edgar_co2_kt = pd.read_csv(url_edgar_co2, header = 6, index_col = [1,2])
            self.df_edgar_co2_kt = self.df_edgar_co2_kt.drop(['substance', 'ISO_CODE'], axis = 1)
            #transpose the matrix so the multi-indexing is on teh columns not rows
            self.df_edgar_co2_kt = self.df_edgar_co2_kt.T


    def emissions_years(self, years):
        """Input list of years or single year.
        Returns data frame with all sectors and countries"""
        return(self.df_edgar_co2_kt.loc[years])


    def emissions_countries(self, countries):
        """Input list of countries or single country
        returns data frame with all sectors and all years"""
        return(self.df_edgar_co2_kt[countries])


    def emissions_sector(self, sector):
        """Input sector (one only) - can't figure out how to make this multiple sectors
        returns data frame with all years and countries"""
        return(self.df_edgar_co2_kt.xs(sector, level = 'sector', axis = 1))


    def emissions_table(self, countries, years, sector):
        """Input the countries, years and sector you want data for
        If you want all years, countries or sectors enter 'all' as that arg"""
        if years == 'all':
            years = [ str(year) for year in range(1970,2016)]

        #if countries == 'all':
        #    countries = :

        if sector = 'all':
            return(self.df_edgar_co2_kt[countries].loc[years])
        else:
            return(self.df_edgar_co2_kt[countries].loc[years].xs(sector, level = 'sector', axis = 1))

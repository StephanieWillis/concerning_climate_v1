class Scenario_Emissions():

    def __init__(self):

        # This is not done yet
        # Might want to use different data sources here.
        #  So lets call the data frames something that makes clear their origin

        url_R26 = 'https://tntcat.iiasa.ac.at/RcpDb/download/R26_bulk.xls'

        if 'df_26' and 'df_45' and 'df_60' and 'df_85' not in globals():
            print("Reading URL again")

            global df_26
            df_26 = pd.read_csv(url_R26, header = 0, index_col = [0,2],
                                 nrows = 18, skiprows = list(range(1,12)),
                                 usecols = list(range(16)))
            #convert values to giga tonees of CO2 from Pg of Carbon.
            #molecular weight of Co2 = 44, molecular weight of carbon = 12
            #change unit heading so it says that those values are in GtCO2/year
            df_26.drop(['Scenario'], axis = 1, inplace=True)

        else:
            print('Using global df variable')


        self.df_26 = df_26
        #print(self.df_edgar_co2_kt)


    def scen_years(self, years):
        """Input list of years or single year.
        Returns data frame with all sectors and countries"""

        return self.df_26[years]


    def scen_countries(self, countries):
        """Input list of countries or single country
        returns data frame with all sectors and all years"""
        countries = sorted(countries)
        return self.df_26.loc[countries]


    def scen_sector(self, sectors):
        """Input sector (one only) - can't figure out how to make this multiple sectors
        returns data frame with all years and countries"""

        All = slice(None)
        sectors = sorted(sectors)
        print(sectors)
        return self.df_26.loc[(All, sectors), All]


    def scen_table(self, countries, years, sectors):
        """Input the countries, years and sector you want data for
        If you want all years, countries or sectors enter 'all' as that arg"""

        All = slice(None)

        if years == 'all' or years == 'All':
            years = All

        if countries == 'all' or countries == 'All':
            countries = All

        if sectors == 'all' or sectors == 'All':
            sectors = All

        return self.df_26.loc[(countries, sectors),years]

#define a plotting method (not a class). It should take a time ranges, and df's
#as inputs and plot the approprieat graphs

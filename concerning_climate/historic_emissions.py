#Lets start with importing the whole data frame from the annual emissions csv
#then lets make a function which manipulates it to only give the data we want
import pandas as pd
import numpy as np
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt

#as a next step try making an emisisons class and make these two children of that

class Historic_Emissions(object):

    def __init__(self, name):
        self.name = name
        #  Might want to use different data sources here.
        #  So lets call the data frames something that makes clear their origin

        if 'df_h' not in globals():
            print("Reading URL again")
            url_edgar_co2= 'http://edgar.jrc.ec.europa.eu/booklet2017/EDGARv432_FT2016_CO2_total_emissions_1970-2016.csv'
            #  Numbers in this sheet only include CO2 emissions
            #  They are in ktonnes of CO2 per year when read in
            # Converted to Gtonnes here for more managable numbers

            global df_h
            df_h = pd.read_csv(url_edgar_co2, header = 6, index_col = [1,2])

            #All CO2 so no need to keep label
            df_h.drop(['substance', 'ISO_CODE'], axis = 1, inplace=True)

            #change units from ktonnes to Giga tonnes
            df_h = df_h/10**6

            #Add per country totals across all sectors
            for country in set(df_h.index.get_level_values(0)):
                sector_sum = df_h.loc[country].sum(axis = 0)
                df_h.loc[(country, 'All sectors'), slice(None)] =  sector_sum
            df_h.sort_index(level=0, inplace = True)

            #Add totals over all time period
            df_h['Total between 1970 and 2016 (Gt CO2)'] =  df_h.sum(axis=1)


            #convert column heading years to integers
            df_h.columns.values[:len(df_h.columns)-1] = \
            list(map(int,df_h.columns.values[:len(df_h.columns)-1]))


        else:
            print('Using global df variable')

        self.df_edgar_co2_Gt = df_h
        #print(self.df_edgar_co2_kt)

    def countries_reminder(self):
        #would be nicer to make a search function but this will do for now
        countries = sorted(set(self.df_edgar_co2_Gt.index.get_level_values(0)))
        return countries

    def countries_search(self):
        """takes input country and finds full name in the list.
        Thus allows user to get name a bit wrong and it can still work"""
        pass

    def hist_table(self, countries = 'all', years = 'all', sectors = 'all'):
        """Input the countries, years and sector you want data for
        If you want all years, countries or sectors enter can leave argument blank or input 'all'"""

        All = slice(None)

        if years == 'all' or years == 'All':
            years = All

        if countries == 'all' or countries == 'All':
            countries = All

        if sectors == 'all' or sectors == 'All':
            sectors = All

        return self.df_edgar_co2_Gt.loc[(countries, sectors),years]

    def plot_pie(self, country, year):
        """plots the sector breakdown in the given year. Option to put
        'all' as argument for year to give the breakdown for the whole period"""

        #ideally produce a title specifying what country and year.
        df_pie = self.hist_table([country], [year], 'all')

        labels = list(df_pie.index.get_level_values(1))[1:] #list of labels excluding 'all sectors'
        sizes = list(df_pie[year])[1:]/df_pie[year][0]*100 #list of sizes of sectors
        #colors = #can always leave this to default
        #explode = (0.05, 0, 0, 0, 0)  could add functionality to explode given sector

        #set up chart and plot
        fig_pie, ax_pie = plt.subplots()
        patches, texts, autotexts = ax_pie.pie(sizes,
                                    labels=labels, autopct='%1.0f%%', shadow=False,
                                    startangle=90, pctdistance = 0.7 )
        #format plot

        title = r'Breakdown of $CO_2$ emissions by sector in {} during {}.'.format(country, year)
        ax_pie.set_title(title)
        ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        proptease_percents = fm.FontProperties(weight = 'bold')
        proptease_percents.set_size('x-large')
        plt.setp(autotexts, fontproperties=proptease_percents)
        proptease_labels = fm.FontProperties()
        proptease_labels.set_size('x-large')
        plt.setp(texts, fontproperties=proptease_labels)

        #Could specify whether you want it to
        #save the resulting figure plt.savefig('CO2_equivalent_breakdown.png', dpi=50)

        plt.show()

    def plot_area_sectors(self, country, year_start = 1970, year_end = 2017, sectors_off = False):
        """plot how emisisons have changed over the statedtime period.
        If sectors_on is true then include sector breakdown"""

        years = list(range(year_start,year_end))

        if sectors_off ==False:
            sectors = ['Buildings', 'Non-combustion', 'Other industrial combustion', 'Power Industry', 'Transport']
        else:
            sectors = ['All sectors']

        #hist_table returns a multi indexed data frame.
        #We only want to look at a single country here so reduce dimensionality
        df_area_sectors= self.hist_table([country], years, sectors).loc[country]
        df_area_sectors.T.plot.area()
        title = r'Evolution of $CO_2$ emissions by sector in {} .'.format(country)
        plt.title(title)
        plt.legend()
        plt.xlabel('\nYear')
        plt.ylabel('Annual $\mathregular{CO_{2}}$ Emissions \n(Gigatonnes of $\mathregular{CO_{2}}$)')
        plt.xlim(year_start, year_end-1) #this doesn't work at the moment because the years are strings. This is going to be a consistent problem so lets sort it out
        plt.show()

        #(df_area_sectors.iloc[1:len(rows)].T.plot.area())
        #plt.legend(rows[1:20])
        #plt.show()


    def plot_area_countries(self, countries, sector = 'All sectors', year_start = 1970, year_end = 2017):
        """plot evolution of emissions in listed countries over
         the stated time period. Can be for all sectors or can choose 1 single sector"""

        years = list(range(year_start,year_end))

        df_area_countries = self.hist_table(countries, years, [sector]).xs(sector, level = 1)
        df_area_countries.T.plot.area()
        title = r'Evolution of $CO_2$ emissions from {} .'.format(sector)
        plt.title(title)
        plt.legend()
        plt.xlabel('\nYear')
        plt.ylabel('Annual $\mathregular{CO_{2}}$ Emissions \n(Gigatonnes of $\mathregular{CO_{2}}$)')
        plt.xlim(year_start, year_end-1) #this doesn't work at the moment because the years are strings. This is going to be a consistent problem so lets sort it out
        plt.show()

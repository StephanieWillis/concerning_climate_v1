from nose.tools import *
from concerning_climate.historic_emissions import Historic_Emissions
import random
import numpy.testing as npt
#from concerning_climate.scenario_emissions import Scenario_Emissions

def test_countries_reminder():
    countries_reminder_trial = Historic_Emissions("Countries reminder trial")
    countries = countries_reminder_trial.countries_reminder()
    print(countries)

def test_hist_table():
    #check that a variety of arguments works
    table_trial = Historic_Emissions("Table trial")
    table_trial.hist_table(['Somalia'], [1991], ['Transport'])
    table_trial.hist_table(['Somalia', 'Algeria'], [1991, 1993, 1995], ['Transport', 'Buildings'])
    table_trial.hist_table('all', [1991, 1993, 1995], ['Transport'])
    table_trial.hist_table(['Somalia', 'Algeria'], 'all', 'Transport')
    table_trial.hist_table(['Somalia', 'Algeria'], [1991, 1993, 1995], 'all')
    table_trial.hist_table('all', [1991, 1993, 1995], 'all')
    table_trial.hist_table(['Somalia', 'Algeria'], 'all', 'all')
    table_trial.hist_table('all', 'all', 'Transport')
    table_trial.hist_table('all', 'all', 'All')

    #check the suming of the sectors gives the expected output
    df_canada = table_trial.hist_table(['Canada'], 'all', 'all')
    result = df_canada.loc[(['Canada'], ['Non-combustion', 'Transport',
                             'Other industrial combustion', 'Power Industry',
                              'Buildings']), slice(None)].sum(axis = 0)


    year = random.randint(1970, 2016)
    npt.assert_almost_equal(result[year], df_canada.loc[(['Canada'], ['All sectors']), slice(None)][year].item(), decimal = 5)

def test_plot_pie():
    """Produces a sample pie chart"""
    plot_pie_trial = Historic_Emissions("Pie chart trial")
    plot_pie_trial.plot_pie('Bulgaria', 2016)

def test_plot_area_sectors():
    """Produces a sample stacked plot"""
    plot_area_sectors_trial = Historic_Emissions("Area sectors chart trial")
    plot_area_sectors_trial.plot_area_sectors('Canada')

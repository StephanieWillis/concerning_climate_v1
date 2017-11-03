from nose.tools import *
from concerning_climate.world_emissions import Emissions


def test_emissions_year():
    print('Running emisisons year look up test')
    emissions_trial = Emissions("Emissions trial")
    years = [ str(year) for year in range(1970,2016)]
    #ideally put an assert equal in here but tricky currently so resort to printing.
    year_trial.emissions_years('2016')
    year_trial.emissions_years(years)

def test_emissions_countries():
    print('Running emissons country look up test')
    countries_trial = Emissions("Emissions trial")
    countries_trial.emissions_countries('Afghanistan')
    countries_trial.emissions_countries(['Afghanistan', 'Brazil', 'Zimbabwe', 'Canada'])

def test_emissions_sector():
    print('Running emissons sector look up test')
    #all possible sectors tested here
    sector_trial = Emissions("Emissions trial")
    sectors = ['Transport','Other industrial combustion', 'Buildings',
               'Non-combustion', 'Power Industry']
    for sector in sectors:
        sector_trial.emissions_sector(sector)

def test_emissions_countries_sector():
    print('Running emissons sectora and country look up test')
    sector_trial = Emissions("Emissions trial")
    sector_trial.emissions_countries_sector(['Somalia', 'Algeria'], 'Transport')


def test_emissions_table():
    print('Running emissons sector look up test')
    table_trial = Emissions("Emissions trial")
    table_trial.emissions_table(['Somalia'], ['1991'], 'Transport')
    table_trial.emissions_table(['Somalia', 'Algeria'], ['1991', '1993', '1995'], 'Transport')
    table_trial.emissions_table('all', ['1991', '1993', '1995'], 'Transport')
    table_trial.emissions_table(['Somalia', 'Algeria'], :, 'Transport')
    table_trial.emissions_table(['Somalia', 'Algeria'], ['1991', '1993', '1995'], 'all')
    table_trial.emissions_table('all', ['1991', '1993', '1995'], 'all')
    table_trial.emissions_table(['Somalia', 'Algeria'], :, 'all')
    table_trial.emissions_table('all', :, 'Transport')
    table_trial.emissions_table('all', :, 'all')

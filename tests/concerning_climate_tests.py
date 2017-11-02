from nose.tools import *
import concerning_climate

def setup(): # runs before every test method
    print("SETUP!")

def teardown(): #runs after every test method
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")

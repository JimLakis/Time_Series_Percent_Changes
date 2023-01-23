'''
Created on Nov 30, 2022

@author: Jim Lakis

'''

import requests


def return_response_object(url):
    with requests.Session() as s:
        try:
            response_obj = requests.get(url,timeout=3)
            response_obj.raise_for_status() # raise_for_status() returns a HTTP error object if an error has occurred 
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting to the internet:    ",errc)
        except requests.exceptions.TooManyRedirects as errrd:
            print ("Too many redirects:    ",errrd)
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:    ",errh)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:    ",errt)
        except requests.exceptions.RequestException as err: # A "catch all" exception
            print ("Unspecified error occured:    ",err)
    return response_obj

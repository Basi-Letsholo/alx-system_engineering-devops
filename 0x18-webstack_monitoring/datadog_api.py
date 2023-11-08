#!/usr/bin/python3
"""Gets dashboard id from my datadog profile"""

import datadog
from datadog import api
import requests


if __name__ == '__main__':

    api_key = '69af620f28a256c866ba329eaf95fed7'
    app_key = 'dd5a5aef0c3e73fb1c6232f973b2f443f76a8b22'

    options = {
            'api_key': api_key,
            'app_key': app_key
            }

    datadog.initialize(**options)
    dashboard = api.Dashboard.get_all()
    
    list_dash = dashboard['dashboards']
    
    for dash in list_dash:
        dash_id = dash['id']
        print("Dashboard: {} | ID: {}".format(dash['title'], dash_id))

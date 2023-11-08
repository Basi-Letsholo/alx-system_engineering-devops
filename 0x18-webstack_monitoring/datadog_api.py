#!/usr/bin/python3
"""Gets dashboard id from my datadog profile"""

import datadog
from datadog import api
import requests


if __name__ == '__main__':

    api_key = ''
    app_key = ''

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

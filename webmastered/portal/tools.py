import folium
from sentry_sdk import capture_exception

from business.models import Client, Staff

from django.contrib import messages
from django.conf import settings

from datetime import datetime, timedelta, date
from threading import Thread
import requests

from dateutil import parser
import pycountry
import pandas as pd


def is_client(this_user):
    if Client.objects.filter(user=this_user):
        return True
    return False


def is_staff(this_user):
    if Staff.objects.filter(user=this_user):
        return True
    return False


def get_client(this_user):
    return Client.objects.get(user=this_user)


class Droplet:
    client = None
    request = None

    region = {
        'timestamp': float(),
        'data': str()
    }
    status = {
        'timestamp': float(),
        'data': None
    }
    memory = {
        'timestamp_total': float(),
        'total': None,
        'timestamp_avail': float(),
        'avail': None
    }
    cpu = {
        'timestamp_cores': float(),
        'cores': None,
        'timestamp_load1': float(),
        'load1': None,
        'timestamp_load5': float(),
        'load5': None,
        'timestamp_load15': float(),
        'load15': None,
    }
    disk = {
        'timestamp_total': float(),
        'timestamp_free': float(),
        'total': None,
        'free': None
    }

    def get_memory_available(self):
        metrics_retrieve_timestamp = datetime.now().timestamp()
        api_request_url = "https://api.digitalocean.com/v2/monitoring/metrics/droplet/memory_available"
        api_request_param = {
            'start': str(metrics_retrieve_timestamp),
            'end': str(metrics_retrieve_timestamp),
            'host_id': str(self.client.digitalocean_droplet_id),
        }
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
            params=api_request_param
        )
        api_response_json = api_response.json()
        if (api_response_json['status'] == "success") & (api_response.status_code == 200):
            self.memory['timestamp_avail'] = api_response_json['data']['result'][0]['values'][0][0]
            available_mem_raw = float(api_response_json['data']['result'][0]['values'][0][1])
            available_mem_gb = available_mem_raw / (1024 ** 3)
            self.memory['avail'] = round(available_mem_gb, 2)
        else:
            messages.error(self.request,
                           "Unable to fetch server available RAM. Please contact the WM team if this issue "
                           "continues.")
            raise Exception

    def get_cpu_load1(self):
        metrics_retrieve_timestamp = datetime.now().timestamp()
        api_request_url = "https://api.digitalocean.com/v2/monitoring/metrics/droplet/load_1"
        api_request_param = {
            'start': str(metrics_retrieve_timestamp),
            'end': str(metrics_retrieve_timestamp),
            'host_id': str(self.client.digitalocean_droplet_id),
        }
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
            params=api_request_param
        )
        api_response_json = api_response.json()
        if (api_response_json['status'] == "success") & (api_response.status_code == 200):
            load1_raw = float(api_response_json['data']['result'][0]['values'][0][1])
            load1_percent = (load1_raw / (self.cpu['cores'])) * 100
            self.cpu['timestamp_load1'] = api_response_json['data']['result'][0]['values'][0][0]
            self.cpu['load1'] = load1_percent
        else:
            messages.error(self.request,
                           "Unable to fetch server CPU load avg (1 min). Please contact the WM team if this issue "
                           "continues.")
            raise Exception

    def get_cpu_load5(self):
        metrics_retrieve_timestamp = datetime.now().timestamp()
        api_request_url = "https://api.digitalocean.com/v2/monitoring/metrics/droplet/load_5"
        api_request_param = {
            'start': str(metrics_retrieve_timestamp),
            'end': str(metrics_retrieve_timestamp),
            'host_id': str(self.client.digitalocean_droplet_id),
        }
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
            params=api_request_param
        )
        api_response_json = api_response.json()
        if (api_response_json['status'] == "success") & (api_response.status_code == 200):
            load5_raw = float(api_response_json['data']['result'][0]['values'][0][1])
            load5_percent = (load5_raw / (self.cpu['cores'])) * 100
            self.cpu['timestamp_load5'] = api_response_json['data']['result'][0]['values'][0][0]
            self.cpu['load5'] = load5_percent
        else:
            messages.error(self.request,
                           "Unable to fetch server CPU load avg (5 min). Please contact the WM team if this issue "
                           "continues.")
            raise Exception

    def get_cpu_load15(self):
        metrics_retrieve_timestamp = datetime.now().timestamp()
        api_request_url = "https://api.digitalocean.com/v2/monitoring/metrics/droplet/load_15"
        api_request_param = {
            'start': str(metrics_retrieve_timestamp),
            'end': str(metrics_retrieve_timestamp),
            'host_id': str(self.client.digitalocean_droplet_id),
        }
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
            params=api_request_param
        )
        api_response_json = api_response.json()
        if (api_response_json['status'] == "success") & (api_response.status_code == 200):
            load15_raw = float(api_response_json['data']['result'][0]['values'][0][1])
            load15_percent = (load15_raw / (self.cpu['cores'])) * 100
            self.cpu['timestamp_load15'] = api_response_json['data']['result'][0]['values'][0][0]
            self.cpu['load15'] = load15_percent
        else:
            messages.error(self.request,
                           "Unable to fetch server CPU load avg (15 min). Please contact the WM team if this issue "
                           "continues.")
            raise Exception

    def get_filesystem_free(self):
        metrics_retrieve_timestamp = datetime.now().timestamp()
        api_request_url = "https://api.digitalocean.com/v2/monitoring/metrics/droplet/filesystem_free"
        api_request_param = {
            'start': str(metrics_retrieve_timestamp),
            'end': str(metrics_retrieve_timestamp),
            'host_id': str(self.client.digitalocean_droplet_id),
        }
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
            params=api_request_param
        )
        api_response_json = api_response.json()
        if (api_response_json['status'] == "success") & (api_response.status_code == 200):
            free_space_bytes = float(api_response_json['data']['result'][0]['values'][0][1])
            free_space_gbytes = free_space_bytes / (1024 ** 3)
            self.disk['timestamp_free'] = api_response_json['data']['result'][0]['values'][0][0]
            self.disk['free'] = round(free_space_gbytes, 2)
        else:
            messages.error(self.request,
                           "Unable to fetch server free storage space. Please contact the WM team if this issue "
                           "continues.")
            raise Exception

    def get_hardware(self):
        api_request_url = "https://api.digitalocean.com/v2/droplets/" + str(self.client.digitalocean_droplet_id)
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.DIGITALOCEAN_ACCESS_TOKEN),
        }
        api_response = requests.get(
            api_request_url,
            headers=api_request_headers,
        )
        api_response_json = api_response.json()
        api_response_timestamp = parser.parse(api_response.headers['Date']).timestamp()
        if api_response.status_code == 200:
            status = api_response_json['droplet']['status']
            memory_mb = api_response_json['droplet']['memory']
            vcpus = api_response_json['droplet']['vcpus']
            disk = api_response_json['droplet']['disk']
            region_slug = api_response_json['droplet']['region']['slug']

            self.status['timestamp'] = api_response_timestamp
            self.status['data'] = status

            self.memory['timestamp_total'] = api_response_timestamp
            self.memory['total'] = memory_mb / 1024

            self.cpu['timestamp_cores'] = api_response_timestamp
            self.cpu['cores'] = vcpus

            self.disk['timestamp_total'] = api_response_timestamp
            self.disk['total'] = disk

            self.region['timestamp'] = api_response_timestamp
            self.region['data'] = self.get_region(region_slug)
        else:
            raise Exception

    def get_region(self, region_slug):
        match region_slug:
            case "nyc1" | "nyc2" | "nyc3":
                return "New York City, United States"
            case "ams2" | "ams3":
                return "Amsterdam, the Netherlands"
            case "sfo1" | "sfo2" | "sfo3":
                return "San Francisco, United States"
            case "sgp1":
                return "Singapore"
            case "lon1":
                return "London, United Kingdom"
            case "fra1":
                return "Frankfurt, Germany"
            case "tor1":
                return "Toronto, Canada"
            case "blr1":
                return "Bangalore, India"
            case _:
                messages.error(self.request,
                               "Unable to fetch server region. Please contact the WM team if this issue continues.")
                return "Unknown"

    def __init__(self, request, client):
        self.request = request
        self.client = client
        try:
            threads = [Thread(target=self.get_hardware()), Thread(target=self.get_filesystem_free()),
                       Thread(target=self.get_cpu_load1()), Thread(target=self.get_cpu_load5()),
                       Thread(target=self.get_cpu_load15()), Thread(target=self.get_memory_available())]
            for _ in range(6):
                threads[_].start()
            for t in threads:
                t.join()
        except Exception as e:
            messages.error(self.request,
                           "Unable to fetch server metrics. Please contact the WM team if this issue continues.")


class Cloudflare:
    request = None
    client = None

    httpRequest1hHistoryLimitDays = settings.HTTP_REQUESTS_1H_GROUPS_HISTORY_LIMIT_DAYS
    firewallEventsAdaptiveLimitDays = settings.FIREWALL_EVENTS_ADAPTIVE_HISTORY_LIMIT_DAYS

    browserMapElement = {
        'pageViews': None,
        'browserFamily': None,
    }

    countryMapElement = {
        'bytes': None,
        'clientCountry': None,
        'requests': None,
        'threats': None,
        'countryMap': []
    }

    httpRequest1hElement = {
        'epoch': float(),
        'avg_bytes': None,
        'unique_ip_count': None,
        'tot_pageViews': None,
        'tot_threats': None,
        'browserMap': [],
        'countryMap': []
    }

    httpRequest1dElement = {
        'epoch': float(),
        'avg_bytes': None,
        'unique_ip_count': None,
        'tot_pageViews': None,
        'tot_threats': None,
        'tot_requests': None,
        'browserMap': [],
        'countryMap': []
    }

    firewallEventElement = {
        'action': str(),
        'clientASNDescription': str(),
        'clientCountryName': str(),
        'clientCountryCode': str(),
        'requestedHost': str(),
        'requestedPath': str(),
        'epoch': float(),
        'userAgent': str()
    }

    httpRequests1hGroups = []
    httpRequests1dGroups = None

    httpRequests1dChoroplethMap = None
    httpRequests1hGroupsTables = []

    firewallEventsHistory = []
    firewallEventsHistoryTable = pd.DataFrame()

    def query_httpRequests1hGroups(self, date):
        httpRequests1hGroups_GraphQL = """
{
  viewer {
    zones(filter: { zoneTag: "%s" }) {
      httpRequests1hGroups(
        limit: 10000
        # 3 days of history can be retrieved...
        filter: { date: "%s" }
      ) {
        avg {
          # avg number of bytes transferred in this interval (1h)
          bytes
        }
        dimensions {
          # datetime of this interval
          datetime
        }
        uniq {
          # number of unique IPs
          uniques
        }
        sum {
          browserMap {
            pageViews
            uaBrowserFamily
          }
          countryMap {
            clientCountryName
            bytes
            threats
            requests
          }
          pageViews
          threats
        }
      }
    }
  }
}
        """ % (self.client.cloudflare_zone_id, date.strftime("%Y-%m-%d"))
        api_request_url = "https://api.cloudflare.com/client/v4/graphql"
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.CLOUDFLARE_API_TOKEN),
        }
        api_response = requests.post(
            url=api_request_url,
            headers=api_request_headers,
            json={'query': httpRequests1hGroups_GraphQL}
        )
        api_response_json = api_response.json()
        response_data = api_response_json['data']['viewer']['zones'][0]['httpRequests1hGroups']
        day_output = []
        for hour_data in response_data:
            this_httpRequest1hElement = self.httpRequest1hElement.copy()
            this_httpRequest1hElement['epoch'] = parser.parse(hour_data['dimensions']['datetime']).timestamp()
            this_httpRequest1hElement['avg_bytes'] = hour_data['avg']['bytes']
            this_httpRequest1hElement['unique_ip_count'] = hour_data['uniq']['uniques']
            this_httpRequest1hElement['tot_pageViews'] = hour_data['sum']['pageViews']
            this_httpRequest1hElement['tot_threats'] = hour_data['sum']['threats']

            for browser in hour_data['sum']['browserMap']:
                this_browserMapElement = self.browserMapElement.copy()
                this_browserMapElement['pageViews'] = browser['pageViews']
                this_browserMapElement['browserFamily'] = browser['uaBrowserFamily']
                this_httpRequest1hElement['browserMap'].append(this_browserMapElement)

            for country in hour_data['sum']['countryMap']:
                this_countryMapElement = self.countryMapElement.copy()
                this_countryMapElement['bytes'] = country['bytes']
                this_countryMapElement['clientCountry'] = country['clientCountryName']
                this_countryMapElement['requests'] = country['requests']
                this_countryMapElement['threats'] = country['threats']
                this_httpRequest1hElement['countryMap'].append(this_countryMapElement)

            day_output.append(this_httpRequest1hElement)
        return day_output

    def query_httpRequests1dGroups(self, date):
        httpRequests1dGroups_GraphQL = """
{
viewer {
    zones(filter: {zoneTag: "%s"}) {
      httpRequests1dGroups(
        limit: 10000,
        # 3 days of history can be retrieved...
        filter: {date: "%s"}
      ) {
        avg{
          bytes
        }
        dimensions{
          date
        }
        uniq{
          uniques
        }
        sum {
          pageViews
          requests
          threats
          countryMap{
            bytes
            clientCountryName
            requests
            threats
          }
        }
      } 
    }
}
}
        """ % (self.client.cloudflare_zone_id, date.strftime("%Y-%m-%d"))
        api_request_url = "https://api.cloudflare.com/client/v4/graphql"
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.CLOUDFLARE_API_TOKEN),
        }
        api_response = requests.post(
            url=api_request_url,
            headers=api_request_headers,
            json={'query': httpRequests1dGroups_GraphQL}
        )
        api_response_json = api_response.json()
        response_data = api_response_json['data']['viewer']['zones'][0]['httpRequests1dGroups'][0]
        day_output = []
        this_httpRequest1dElement = self.httpRequest1dElement.copy()
        this_httpRequest1dElement['epoch'] = parser.parse(api_response.headers['Date']).timestamp()
        this_httpRequest1dElement['avg_bytes'] = response_data['avg']['bytes']
        this_httpRequest1dElement['unique_ip_count'] = response_data['uniq']['uniques']
        this_httpRequest1dElement['tot_pageViews'] = response_data['sum']['pageViews']
        this_httpRequest1dElement['tot_threats'] = response_data['sum']['threats']
        this_httpRequest1dElement['tot_requests'] = response_data['sum']['requests']
        this_httpRequest1dElement['countryMap'] = []
        for country in response_data['sum']['countryMap']:
            this_countryMapElement = self.countryMapElement.copy()
            this_countryMapElement['bytes'] = country['bytes']
            this_countryMapElement['clientCountry'] = country['clientCountryName']
            this_countryMapElement['requests'] = country['requests']
            this_countryMapElement['threats'] = country['threats']
            this_httpRequest1dElement['countryMap'].append(this_countryMapElement)
        day_output.append(this_httpRequest1dElement)
        return day_output

    def query_firewallEventsAdaptive(self, date):
        firewallEventsAdaptive_GraphQL = """
{
  viewer {
    zones(filter: {zoneTag: "%s"}) {
      firewallEventsAdaptive(
        limit: 10000
        # 14 days of history can be retrieved...
        filter: {date: "%s"}
      ) {
        action
        clientASNDescription
        clientCountryName
        clientIP
        clientIPClass
        clientRequestHTTPHost
        clientRequestPath
        clientRequestQuery
        datetime
        userAgent
      }
    }
  }
}
        """ % (self.client.cloudflare_zone_id, date.strftime("%Y-%m-%d"))
        api_request_url = "https://api.cloudflare.com/client/v4/graphql"
        api_request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(settings.CLOUDFLARE_API_TOKEN),
        }
        api_response = requests.post(
            url=api_request_url,
            headers=api_request_headers,
            json={'query': firewallEventsAdaptive_GraphQL}
        )
        api_response_json = api_response.json()
        response_data = api_response_json['data']['viewer']['zones'][0]['firewallEventsAdaptive']
        day_output = []
        for event in response_data:
            this_firewallEventElement = self.firewallEventElement.copy()
            this_firewallEventElement['action'] = event['action']
            this_firewallEventElement['clientASNDescription'] = event['clientASNDescription']
            try:
                this_firewallEventElement['clientCountryName'] = pycountry.countries.get(
                    alpha_2=event['clientCountryName']).name
                this_firewallEventElement['clientCountryCode'] = pycountry.countries.get(
                    alpha_2=event['clientCountryName']).alpha_3
            except:
                this_firewallEventElement['clientCountryName'] = "-"
                this_firewallEventElement['clientCountryCode'] = "-"
            this_firewallEventElement['requestedHost'] = event['clientRequestHTTPHost']
            this_firewallEventElement['requestedPath'] = event['clientRequestPath']
            this_firewallEventElement['epoch'] = parser.parse(event['datetime']).timestamp()
            this_firewallEventElement['userAgent'] = event['userAgent']
            day_output.append(this_firewallEventElement)
        return day_output

    def get_httpRequests1hGroups(self):
        datenow = date.today()
        self.httpRequests1hGroups = []
        for _ in range(self.httpRequest1hHistoryLimitDays):
            query_date = datenow - timedelta(days=_)
            self.httpRequests1hGroups.append(self.query_httpRequests1hGroups(query_date))

    def get_httpRequest1dGroup(self):
        datenow = date.today()
        self.httpRequests1dGroups = self.query_httpRequests1dGroups(datenow)[0]

    def get_firewallEventsAdaptive(self):
        datenow = date.today()
        self.firewallEventsHistory = []
        for _ in range(self.firewallEventsAdaptiveLimitDays):
            query_date = datenow - timedelta(days=_)
            self.firewallEventsHistory.append(self.query_firewallEventsAdaptive(query_date))

    def countryMapToChoroplethMap(self):
        map_data_dict_list = []
        for country in self.httpRequests1dGroups['countryMap']:
            try:
                this_country = {
                    'ISO_A3': pycountry.countries.get(alpha_2=country['clientCountry']).alpha_3,
                    'Country Code': pycountry.countries.get(alpha_2=country['clientCountry']).alpha_3,
                    'Country Name': pycountry.countries.get(alpha_2=country['clientCountry']).name,
                    'Bytes Transferred': country['bytes'],
                    'Requests': country['requests'],
                    'Threats': country['threats'],
                }
                map_data_dict_list.append(this_country)
            except:
                pass
        map_data_df = pd.DataFrame(map_data_dict_list).set_index('ISO_A3')
        choroplethMap = folium.Map(
            max_bounds=True,
        )
        geojson = requests.get("https://raw.githubusercontent.com/AshKyd/geojson-regions/master/countries/110m/all"
                               ".geojson").json()
        for country in geojson['features']:
            if country['properties']['iso_a3'] in map_data_df.index:
                country['properties']['cloudflare_bytes'] = float(
                    map_data_df.loc[country['properties']['iso_a3']]['Bytes Transferred'])
                country['properties']['cloudflare_requests'] = float(
                    map_data_df.loc[country['properties']['iso_a3']]['Requests'])
                country['properties']['cloudflare_threats'] = float(
                    map_data_df.loc[country['properties']['iso_a3']]['Threats'])
            else:
                country['properties']['cloudflare_bytes'] = float(0)
                country['properties']['cloudflare_requests'] = float(0)
                country['properties']['cloudflare_threats'] = float(0)
        map = folium.Choropleth(
            geo_data=geojson,
            data=map_data_df,
            columns=['Country Code', 'Requests'],
            key_on='feature.properties.iso_a3',
            fill_color='YlGnBu',
            fill_opacity=0.7,
            line_opacity=0.2,
            reset=True,
            nan_fill_opacity=0,
            legend_name="Requests",
        ).add_to(choroplethMap)
        folium.GeoJsonTooltip(
            fields=['name', 'cloudflare_bytes', 'cloudflare_requests', 'cloudflare_threats'],
            aliases=["", "Bytes", "Requests", "Threats"]
        ).add_to(map.geojson)
        self.httpRequests1dChoroplethMap = choroplethMap._repr_html_()

    def get_httpRequests1hGroupsTables(self):
        self.httpRequests1hGroupsTables = []
        for i, group in enumerate(self.httpRequests1hGroups):
            group_df = pd.DataFrame(group)
            group_df.drop('browserMap', inplace=True, axis=1)
            group_df.drop('countryMap', inplace=True, axis=1)
            group_df.drop('avg_bytes', inplace=True, axis=1)
            if i == 0:
                group_df['epoch'] = pd.to_datetime(group_df['epoch'], unit='s').dt.time
            else:
                group_df['epoch'] = pd.to_datetime(group_df['epoch'], unit='s')
            group_df.rename(
                columns={
                    'epoch': 'Time',
                    'unique_ip_count': 'Unique Visitors',
                    'tot_pageViews': 'Views',
                    'tot_threats': 'Threats'
                },
                inplace=True,
            )
            self.httpRequests1hGroupsTables.append(
                group_df.to_html(
                    classes='wm-httpRequests1hGroupTable compact hover row-border stripe',
                    index=False,
                )
            )

    def get_firewallEventsHistoryTables(self):
        self.firewallEventsHistoryTable = str()
        firewallEvents_list = []
        for day in self.firewallEventsHistory:
            if day:
                for event in day:
                    firewallEvents_list.append(event)
        firewallEvents_df = pd.DataFrame(firewallEvents_list)
        firewallEvents_df = firewallEvents_df[['epoch', 'clientASNDescription', 'clientCountryName', 'clientCountryCode', 'userAgent', 'requestedHost', 'requestedPath', 'action']]
        firewallEvents_df['epoch'] = pd.to_datetime(firewallEvents_df['epoch'], unit='s')
        firewallEvents_df.rename(
            columns={
                'epoch': 'Timestamp',
                'clientASNDescription': 'Client Description',
                'clientCountryName': 'Client Country Name',
                'clientCountryCode': 'Client Country Code',
                'userAgent': 'Client User Agent',
                'requestedHost': 'Requested Host',
                'requestedPath': 'Requested Path',
                'action': 'Firewall Action'
            },
            inplace=True,
        )
        self.firewallEventsHistoryTable = firewallEvents_df.to_html(
                classes='wm-firewallEventsHistoryTable compact hover row-border stripe',
                index=False,
        )

    def __init__(self, request, client):
        self.request = request
        self.client = client
        try:
            primary_methods = [
                Thread(target=self.get_httpRequests1hGroups()),
                Thread(target=self.get_httpRequest1dGroup()),
                Thread(target=self.get_firewallEventsAdaptive()),
           ]
            secondary_methods = [
                Thread(target=self.countryMapToChoroplethMap()),
                Thread(target=self.get_httpRequests1hGroupsTables()),
                Thread(target=self.get_firewallEventsHistoryTables()),
            ]

            for _ in range(len(primary_methods)):
                primary_methods[_].start()
            for t in primary_methods:
                t.join()

            for _ in range(len(secondary_methods)):
                secondary_methods[_].start()
            for t in secondary_methods:
                t.join()

        except Exception as e:
            capture_exception(e)
            messages.error(self.request,
                           "Unable to fetch website metrics. Please contact the WM team if this issue continues.")

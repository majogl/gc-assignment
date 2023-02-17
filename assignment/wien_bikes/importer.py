import requests
from wien_bikes.config import WIEN_BIKE_API_URL
from wien_bikes.utils import get_address_from_coords

class Importer:
    
    
    def __init__(self):
        self.stations = []
        self._ETL_unempty_stations()
        
        
    def _ETL_unempty_stations(self):
        # An ETL method specific to this assignment. If this was to be actually
        # used, I would go for a more generic approach, splitting the extraction,
        # transformation and sorting into different methods. Or program custom filters.
        response = requests.get(WIEN_BIKE_API_URL)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError
        self.stations = []
        for st in response.json():
            if st['free_bikes'] > 0:
                transf_st = {
                    'id': st['id'],
                    'name': st['name'],
                    'active': st['status'] == 'aktiv',
                    'description': st['description'],
                    'boxes': st['boxes'],
                    'free_boxes': st['free_boxes'],
                    'free_bikes': st['free_bikes'],
                    'free_ratio': st['free_boxes'] / st['boxes'],
                    'coordinates': [st['longitude'], st['latitude']],
                    'address': get_address_from_coords(lat=st['latitude'],lon=st['longitude'])
                }
                self.stations.append(transf_st)
        self.stations = sorted(self.stations, key= lambda k: (int(k['free_bikes'])*-1, k['name']))

    def __str__(self):
        r = ''
        e = 1
        for s in self.stations:
            r += f'ENTRY {e}\n'
            for (k,v) in s.items():
                r += f'{k} ---> {v}\n'
            r += '\n'
            e += 1
        return r
    
    def __repr__(self):
        print(self.__str__())

    def get_stations(self):
        return self.stations

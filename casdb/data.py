
from cassandra.cluster import Cluster
from logger import logger
import json

try:
    cas_clusters = Cluster(['192.168.85.128', '192.168.85.130'])
    cas_db_session = cas_clusters.connect('naqaba')
    logger.info("Target nodes connected")
except Exception as e:
    logger.error(e)


def get_bus_locations(**kwrgs):
    cql_query = 'select company_id, bus_id, bus_serial, ignition, movement, lat, long, speed ' \
                'from vehicle_locations where bus_id=' + "'%s'" % kwrgs['bus_id'] + ' ALLOW FILTERING;'
    data = []
    raw_data = cas_db_session.execute(cql_query)
    columns = raw_data.column_names
    for row in raw_data.current_rows:
        data.append(dict(zip(columns, row)))
    response = json.dumps(data)
    return response
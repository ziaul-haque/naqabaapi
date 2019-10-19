
from cassandra.cluster import Cluster
from logger import logger


try:
    cas_clusters = Cluster(['192.168.85.128', '192.168.85.130'])
    cas_db_session = cas_clusters.connect('naqaba')
    logger.info("Target nodes connected")
except Exception as e:
    logger.error(e)

def get_bus_locations(bus_id, company_id, start, end):
    cql_query = 'select company_id, bus_id, bus_serial, ignition, movement, lat, long, speed ' \
                'from vehicle_locations where bus_id={0} and company_id= {1} '.format(bus_id, company_id)
    if start and end:
        cql_query = cql_query + ' and record_time >= {0} and record_time <= {1}'.format(start,end)
    data = cas_db_session.execute(cql_query)
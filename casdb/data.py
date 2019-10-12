
from cassandra.cluster import Cluster
from logger import logger

try:
    target_clusters = Cluster(cassandra_nodes)
    logger.info("Target nodes connected")
except Exception as e:
    logger.error(e)
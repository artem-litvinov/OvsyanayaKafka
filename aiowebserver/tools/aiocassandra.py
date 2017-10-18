import asyncio
from aiocassandra import aiosession
from cassandra.cluster import Cluster

class AIOCassandra(object):
    __init__(self, host='localhost'):
        self.__cluster = Cluster([host])
    
    def connect(self, loop, keyspace='default'):
        if loop is None:
            loop = asyncio.get_event_loop()
        aiosession(self.__session, loop=loop)
        self.__session = cluster.connect(keyspace)

    async def get_from_table_by_id(self, table, id):
        if not table or not id:
            raise RuntimeError, 'table or id is None'
        return await (self.__session.execute_future("SELECT * FROM %s WHERE uid='%s'" % (table, uid)))
        

if __name__ == "__main__":
    try:
        CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
    except KeyError as err:
        print(err, "Please set CASSANDRA_HOST environment variable")
        raise
    cassandra = AIOCassandra(CASSANDRA_HOST)
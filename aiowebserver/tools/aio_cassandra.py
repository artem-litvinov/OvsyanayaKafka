import os
import asyncio
from aiocassandra import aiosession
from cassandra.cluster import Cluster

loop = asyncio.get_event_loop()

class AIOCassandra(object):
    def __init__(self, host='localhost'):
        self.__cluster = Cluster([host])
    
    def connect(self, loop, keyspace='default'):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.__session = self.__cluster.connect(keyspace)
        aiocassandra.aiosession(self.__session, loop=loop)

    async def get_from_table_by_id(self, table, id):
        if not table or not id:
            raise RuntimeError('table or id is None')
        return await (self.__session.execute_future("SELECT * FROM %s WHERE uid='%s'" % (table, id)))

async def main():
    try:
        CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
    except KeyError as err:
        print(err, "Please set CASSANDRA_HOST environment variable")
        # raise
        CASSANDRA_HOST = 'localhost'
    cassandra = AIOCassandra(CASSANDRA_HOST)
    cassandra.connect(loop, keyspace='users')
    print((await cassandra.get_from_table_by_id('users', '1')))

if __name__ == "__main__":
    print('entering test producer')
    loop.run_until_complete(main())
    loop.close()

import sys
sys.path.append('./gen-py')

from kafka_data.ttypes import Kafka_Data

from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

def run():
    data = Kafka_Data("phone", "+79997305889", "test message from space to m0sk1t phone")

    print data

    transportOut = TTransport.TMemoryBuffer()
    protocolOut = TBinaryProtocol.TBinaryProtocol(transportOut)
    data.write(protocolOut)
    bytes = transportOut.getvalue()

    print bytes

    transportIn = TTransport.TMemoryBuffer(bytes)
    protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)

    newData = Kafka_Data()
    newData.read(protocolIn)

    print newData

if __name__ == "__main__":
    run()
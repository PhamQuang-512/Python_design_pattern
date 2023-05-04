from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class Connection(ABC):
    @abstractmethod
    def description(self):
        pass


class OracleConnection(Connection):
    def description(self):
        print("Oracle")


class MySQLConnection(Connection):
    def description(self):
        print("MySQL")


class MongoDBConnection(Connection):
    def description(self):
        print("MongoDB")


class SecureOracleConnection(OracleConnection):
    def description(self):
        print("Secure: ", end="")
        super().description()


class SecureMySQLConnection(MySQLConnection):
    def description(self):
        print("Secure: ", end="")
        super().description()


class SecureMongoDBConnection(MongoDBConnection):
    def description(self):
        print("Secure: ", end="")
        super().description()


class ConnectionType(str, Enum):
    oracle = "Oracle"
    mysql = "mysql"
    mongodb = "mongodb"


class ConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self, type: ConnectionType) -> Connection:
        pass


class SecureFactory(ConnectionFactory):
    def create_connection(self, type: ConnectionType) -> Connection:
        if type is ConnectionType.mysql:
            return SecureMySQLConnection()
        elif type is ConnectionType.oracle:
            return SecureOracleConnection()
        elif type is ConnectionType.mongodb:
            return SecureMongoDBConnection()
        else:
            raise Exception("No connection found!")


if __name__ == "__main__":
    factory = SecureFactory()
    oracle_connection = factory.create_connection(ConnectionType.oracle)
    print(oracle_connection)
    mysql_connection = factory.create_connection(ConnectionType.mysql)
    print(mysql_connection)
    mongodb_connection = factory.create_connection(ConnectionType.mongodb)
    print(mongodb_connection)

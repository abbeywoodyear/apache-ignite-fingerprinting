import helpers.sql_helper as SqlHelper
import helpers.csv_helper as CsvHelper
from pyignite import Client

# establish connection
client = Client()
with client.connect('127.0.0.1', 10800):
    
    filename = "../pcaps/gb4_popinabox_100k_parsed_new.csv"

    # delete table
    client.sql("DROP TABLE Fingerprint")

    print("Getting the csv...")
    table_values = CsvHelper.get_table_values(filename)

    updated_values = CsvHelper.get_count_and_id(table_values)

    SqlHelper.create_table_from_values(updated_values, client)

    # delete table
    client.sql("DROP TABLE Fingerprint")

    with client.sql('SELECT ID, PayLen FROM Fingerprint ORDER BY PayLen DESC LIMIT 10') as cursor:
        print('Packets with highest payloads:')
        for row in cursor:
            print(row)

    with client.sql('SELECT ID, Count FROM Fingerprint ORDER BY Count DESC LIMIT 10') as cursor:
        print('Packets with highest count:')
        for row in cursor:
            print(row)

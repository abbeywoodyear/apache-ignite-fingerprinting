
FINGERPRINT_CREATE_TABLE = '''CREATE TABLE Fingerprint (
    ID LONG(20) PRIMARY KEY,
    IPVer INT(1),
    L3Proto INT(1),
    L3ToS INT(2),
    L3Len INT(5),
    L3ID INT(6),
    L3Frag INT(1),
    L3TTL INT(4),
    L3Chksum INT(5),
    L3SrcIP CHAR(50),
    L3DstIP CHAR(50),
    L4Sport INT(3),
    L4Dport INT(3),
    UDPLen INT(4),
    L4Ack LONG(11),
    L4Seq LONG(2),
    L4Dataofs INT(3),
    L4Window INT(4),
    L4Chksum INT(5),
    L4UrgPtr INT(1),
    L4Options CHAR(16),
    L4MSS INT(3),
    L4_WScale INT(3),
    Flags CHAR(18),
    ICMPType INT(2),
    ICMPCode INT(2),
    PayLen INT(6),
    Count INT(6)
)'''

FINGERPRINT_INSERT = '''INSERT INTO Fingerprint(
    ID, IPVer, L3Proto, L3ToS, L3Len, L3ID, 
    L3Frag, L3TTL, L3Chksum, L3SrcIP, L3DstIP, 
    L4Sport, L4Dport, UDPLen, L4Ack, L4Seq, 
    L4Dataofs, L4Window, L4Chksum, L4UrgPtr, 
    L4Options, L4MSS, L4_WScale, Flags, 
    ICMPType, ICMPCode, PayLen, Count
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

def create_table_from_values(value_list, client):
    # create table
    client.sql(FINGERPRINT_CREATE_TABLE)

    # load data
    for row in value_list:
        if len(row) == 28:
            print(row)
            client.sql(FINGERPRINT_INSERT, query_args=row)

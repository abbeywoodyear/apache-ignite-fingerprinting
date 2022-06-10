import csv, sys

def get_table_values(filename):
    try:
        with open(filename, 'r') as file:
            file_reader = csv.reader(file, delimiter='|')
            # Skip the header
            next(file_reader, None)
            data = list(file_reader)
            fingerprints = []
            for inner_list in data:
                temp_list = []
                for element in inner_list:
                    if element.isdigit():
                        temp_list.append(int(element))
                    else:
                        temp_list.append(element)
                fingerprints.append(temp_list)
            return fingerprints
    except Exception as e:
        print(f'Error: {e}')

def get_count_and_id(value_list):
    value_dict = {}
    count = 0
    for sig in value_list:
        sig_hash = hash(tuple(sig))
        if sig_hash < 0:
            sig_hash += sys.maxsize + 1
        if sig_hash in value_dict:
            # increments count and updates count for sig list
            value_dict[sig_hash] += 1
            sig[len(sig) - 1] = value_dict[sig_hash]
        else:
            # adds count to dict and sig list
            value_dict[sig_hash] = 1
            sig.append(1)
        # inserts hash value to start of list
        sig.insert(0, sig_hash)
        count += 1
        if count > 100000:
            return value_list
    return value_list

# class Sig:
#     def __init__(self,  ID, IPVer, L3Proto, L3ToS, L3Len, 
#         L3ID, L3Frag, L3TTL, L3Chksum, L3SrcIP, L3DstIP, 
#         L4Sport, L4Dport, UDPLen, L4Ack, L4Seq, 
#         L4Dataofs, L4Window, L4Chksum, L4UrgPtr, 
#         L4Options, L4MSS, L4_WScale, Flags, 
#         ICMPType, ICMPCode, PayLen):
#         self.ID = ID
#         self.IPVer = IPVer
#         self.L3Proto = L3Proto
#         self.L3ToS = L3ToS
#         self.L3Len = L3Len
#         self.L3ID = L3ID
#         self.L3Frag = L3Frag
#         self.L3TTL = L3TTL
#         self.L3Chksum = L3Chksum
#         self.L3SrcIP = L3SrcIP
#         self.L3DstIP = L3DstIP
#         self.L4Sport = L4Sport
#         self.L4Dport = L4Dport
#         self.UDPLen = UDPLen
#         self.L4Ack = L4Ack
#         self.L4Seq = L4Seq
#         self.L4Dataofs = L4Dataofs
#         self.L4Window = L4Window
#         self.L4Chksum = L4Chksum
#         self.L4UrgPtr = L4UrgPtr
#         self.L4Options = L4Options
#         self.L4MSS = L4MSS
#         self.L4_WScale = L4_WScale
#         self.Flags = Flags
#         self.ICMPType = ICMPType
#         self.ICMPCode = ICMPCode
#         self.PayLen = PayLen    

#     def __hash__(self):
#         # hash for our list object
#         return hash((self.ID, self.IPVer, self.L3Proto, 
#         self.L3ToS, self.L3Len, self.L3ID, 
#         self.L3Frag, self.L3TTL, self.L3Chksum, 
#         self.L3SrcIP, self.L3DstIP, self.L4Sport, 
#         self.L4Dport, self.UDPLen, self.L4Ack, 
#         self.L4Seq, self.L4Dataofs, self.L4Window, 
#         self.L4Chksum, self.L4UrgPtr, self.L4Options, 
#         self.L4MSS, self.L4_WScale, self.Flags, 
#         self.ICMPType, self.ICMPCode, self.PayLen))

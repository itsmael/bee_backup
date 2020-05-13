import sys
from fdb import services
import fdb

input = sys.argv[0::]

path_1=(input[1])
path_2=(input[2])

con = services.connect(host='localhost', user='sysdba', password='masterkey')
con.backup(path_1 , path_2, metadata_only=False, collect_garbage=True)
backup_report = con.readlines()
con.close()

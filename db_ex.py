from cassandra.cluster import Cluster
import time
import csv
import threading
from logging import exception



cassandra_ip = 'ec2-34-254-44-103.eu-west-1.compute.amazonaws.com'
session = Cluster([cassandra_ip]).connect(keyspace='eden')

def battery():
 with open('battery.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["customer_id", "building_id", "tstamp_record", "battery_state_of_charge", "battery_powerflow_l1", "battery_powerflow_l2", "battery_powerflow_l3"])
    while True:
        time.sleep(5)
        battery_list = session.execute('select customer_id, building_id, tstamp_record, battery.state_of_charge, battery.powerflow_l1 from current_state WHERE asset_id=2000 and customer_id=1 allow filtering')
        for datapoint in battery_list:
            writer.writerow([datapoint.customer_id, datapoint.building_id, datapoint.tstamp_record, datapoint.battery_state_of_charge, datapoint.battery_powerflow_l1])
            print(datapoint)

def real_capacity():
 with open('real_capacity.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ts", "frequency", "power_active", "power_capacity"])
    while True:
        time.sleep(5)
        real_capacity_list = session.execute("select ts, frequency , power_active, power_capacity from fcrn_aggr_timeseries WHERE ts> 'toTimestamp(toDate(now())'  allow filtering")
        for datapoint in real_capacity_list:
            writer.writerow([datapoint.ts, datapoint.frequency, datapoint.power_active, datapoint.power_capacity])



thread1=threading.Thread(target=battery)
thread1.start()

thread2=threading.Thread(target=real_capacity)
thread2.start()

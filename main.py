from scrap_data import scrap_data
from data_flow_to_mysql import flow_data_to_mysql
from get_data_from_mysql import get_table
import time
import schedule

def flow():
    scrap_data()
    time.sleep(1)

    flow_data_to_mysql()
    time.sleep(1)

    data = get_table()
    time.sleep(2)

    print(data)


schedule.every(10).seconds.do(flow)
schedule.every(10).minutes.do(flow)
schedule.every().hour.do(flow)
schedule.every().day.at("10:30").do(flow)
schedule.every(5).to(10).minutes.do(flow)
schedule.every().monday.do(flow)
schedule.every().wednesday.at("13:15").do(flow)
schedule.every().minute.at(":17").do(flow)

while True:
    schedule.run_pending()
    time.sleep(1)
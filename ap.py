import Adafruit_DHT
import pandas as pd
import time as t
sensortype=Adafruit_DHT.DHT22

output=pd.DataFrame()
count=0
while True:
    #print('getting reading')
    humidity4, temperature4=Adafruit_DHT.read_retry(sensortype,4)
    humidity17, temperature17=Adafruit_DHT.read_retry(sensortype,17)
    humidity22, temperature22=Adafruit_DHT.read_retry(sensortype,22)
    EPOCH=t.time()
    output.loc[count,'EPOCH']=EPOCH
    output.loc[count,'temp4']=temperature4
    output.loc[count,'humd4']=humidity4
    output.loc[count,'temp17']=temperature17
    output.loc[count,'humd17']=humidity17
    output.loc[count,'temp22']=temperature22
    output.loc[count,'humd22']=humidity22
    output.to_csv('tempdata.csv')
    #print('finished reading')
    #print('Humidity: '+str(humidity)+' temp: '+str(temperature))
    t.sleep(5)
    count =count+1

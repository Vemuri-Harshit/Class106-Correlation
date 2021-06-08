import plotly.express as px;
import numpy as np;
import csv;

def getDataSource_data(data_path):
    temperature = []
    ice_cream = []

    with open(data_path) as data_file: 
        csv_reader = csv.DictReader(data_file);
        for row in csv_reader : 
            temperature.append(float(row["temperature"]))
            ice_cream.append(float(row["ice-cream"]))

    return{"x": temperature, "y": ice_cream}

def findCorrelation_data(data_source) : 
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation for Ice Cream and temperature is", correlation[0,1])

findCorrelation_data( getDataSource_data("./data_1.csv") )
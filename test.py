import requests
import xml.etree.ElementTree as ET
from lxml import etree

xml = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=Mallow')
with open('irishrail_data.xml', 'w') as f:
        f.write(xml.content.decode())    
if xml.status_code == 200:
    root = etree.fromstring(xml.content)
    
def build_table_row(root):
        list1 = []
        data = []
        for element in root.iter():
                if 'Destination' in  element.tag:
                        if element.tag != '{http://api.irishrail.ie/realtime/}Destinationtime':
                                data.append(element.text)
                elif 'Origin' in  element.tag:
                        if element.tag != '{http://api.irishrail.ie/realtime/}Origintime':
                                data.append(element.text)
                elif 'Exparrival' in element.tag:
                        data.append(element.text)
                elif 'Expdepart' in element.tag:
                        data.append(element.text)
                elif 'Scharrival' in element.tag:
                        data.append(element.text)
                        list1.append(data)
                        data = []
        return list1
        
list1 = build_table_row(root)


def build_html_table(data):
       
        html_code = ""
        html_code += "<h1> Train Stop Timetable </h1>"
        # Styling taken from here  -> https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy
        html_code += "<style> font-family: Arial, Helvetica, sans-serif; border-collapse: collapse; width: 100%;} #customers td, #customers th { border: 1px solid #ddd; padding: 8px; } #customers tr:nth-child(even){background-color: #f2f2f2;} #customers tr:hover {background-color: #ddd;} #customers th { padding-top: 12px; padding-bottom: 12px; text-align: left; background-color: #04AA6D; color: white; } </style>"
        
        html_code += "<table id='customers'>"
        html_code += "<th>Destination</th><th>Origin</th><th>Expected Arrival</th><th>Expected Departure</th><th>Scheduled Arrival</th>"


        for row in data:
                html_code += "<tr>"
                for item in row:
                        html_code += "<td>{}</td>".format(item)
                html_code += "</tr>"

        html_code += "</table>"

        with open("table.html", "w") as file:
                file.write(html_code)
                
build_html_table(list1)
                
                

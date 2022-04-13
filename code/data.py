from netCDF4 import Dataset
import datetime

# 甘肃中电酒泉第四风力发电有限公司
lat_index = 256
lon_index = 269
variable_list = ["lrad", "prec", "pres", "shum", "srad", "temp", "wind"]

with open('data.csv', 'w') as f:
    f.write("ds")
    for variable in variable_list:
        f.write(',' + variable)
    f.write('\n')
    for year in range(2017, 2019):
        for month in range(1, 13):
            dataset = []
            time_data = []
            for name in variable_list:
                data = Dataset("data/" + name + "_ITPCAS-CMFD_V0106_B-01_03hr_010deg_" +
                               str(year) + str(month).zfill(2) + ".nc")
                dataset.append(data.variables[name][:])
                # lat_data = data.variables['lat'][:]
                # lon_data = data.variables['lon'][:]
                time_data = data.variables['time'][:]

            for index in range(len(time_data)):
                f.write(datetime.datetime.utcfromtimestamp((time_data[index]-613608)*3600).strftime("%Y-%m-%d %H:%M:%S"))
                for data in dataset:
                    f.write(',' + str(data[index][lat_index][lon_index]))
                f.write('\n')

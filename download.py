import cdsapi
import datetime

c = cdsapi.Client()

begindate="2021-03-20"
enddate="2021-03-24"

begin_dateobj=datetime(int(begindate.split("-")[0]),int(begindate.split("-")[1]),int(begindate.split("-")[2]))
end_dateobj=datetime(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))

dates=[begin_dateobj + timedelta(days=x) for x in range((end_dateobj-begin_dateobj).days)]

variables=['2m_dewpoint_temperature', '2m_temperature', 'soil_temperature_level_1','total_precipitation', 'volumetric_soil_water_layer_1',]
AOIs=[[58.29, 26.48, 58.27,26.5]]
IDs=['1']

for date in dates:
    for var in variables:
        for AOI in AOIs:
            name=date.strftime('%Y%m/%d')+"_"+var+"_"+IDs[AOIs.index(AOI)]+'.nc'
            c.retrieve(
                'reanalysis-era5-single-levels',
                {
                    'product_type': 'reanalysis',
                    'format': 'netcdf',
                    'year': str(date.year),
                    'month': str(date.month),
                    'variable': var,
                    'day': str(date.day),
                    'time': [
                        '00:00', '01:00', '02:00',
                        '03:00', '04:00', '05:00',
                        '06:00', '07:00', '08:00',
                        '09:00', '10:00', '11:00',
                        '12:00', '13:00', '14:00',
                        '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00',
                        '21:00', '22:00', '23:00',
                    ],
                    'area': AOI,
                },
                name)
            
            
            
     


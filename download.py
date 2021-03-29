import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-land',
    {
        'format': 'netcdf',
        'variable': '2m_dewpoint_temperature',
        'year': '2021',
        'month': '01',
        'day': '01',
        'time': '00:00',
    },
    'download.nc')

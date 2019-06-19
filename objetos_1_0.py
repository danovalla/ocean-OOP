"""
Primer intento de script orientado a objetos.

La idea es que los objetos sean archivos de datos georreferenciados .nc que
pertenecen a la clase 'netcdf'. Las variables que comparten todos son longitud,
latitud y tiempo.

display_metadata: lista las variables del archivo y como opción tambien su
                  metadata.


@juliabock
"""

class Netcdf(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def display_metadata(self):
        import xarray
        archivo = xarray.open_dataset(self.path)
        print(archivo.data_vars)
        query = input('Which variable are you interested in? ')
        while query != '':
            print(archivo[query])
            query = input('Which other variable are you interested in? ')

    def time_mean(self):
        import xarray
        archivo = xarray.open_dataset(self.path)

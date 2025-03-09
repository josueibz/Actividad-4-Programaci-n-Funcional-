def cargar_dataset(archivo):
    import pandas as pd
    import os
    #si se desea agregar un input
    extension = os.path.splitext(archivo)[1].lower()
    #cargar el archivo segun su extension
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return(df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
            raise ValueError('Formato de archivo no soportado',extension)
    
def sust_nulos_ffill(df):
    import pandas as pd
    import numpy as np

    return df.fillna(method='ffill')

def sust_nulos_bfill(df):
    import pandas as pd
    import numpy as np

    return df.fillna(method='bfill')

def sust_nulos_string(df,string_concreto='Valor Desconocido'):
    import pandas as pd
    import numpy as np

    return df.fillna(string_concreto)

def sust_nulos_promedio(df):
    import pandas as pd
    import numpy as np

    cuantitativas = df.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    cuantitativas = cuantitativas.fillna(round(cuantitativas.mean(), 1))
    df = pd.concat([cuantitativas, cualitativas], axis=1)

    return df

def sust_nulos_mediana(df):
    import pandas as pd
    import numpy as np

    cuantitativas = df.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    cuantitativas = cuantitativas.fillna(round(cuantitativas.median(), 1))
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return df

def sust_nulos_constante(df,constante=0):
    import pandas as pd
    import numpy as np

    return df.fillna(constante)

def identificar_nulos(df):
    import pandas as pd
    import numpy as np

    nulos_por_columna = df.isnull().sum()
    nulos_totales = df.isnull().sum().sum()
    return ('Nulos por columna:',nulos_por_columna,'Nulos totales:',nulos_totales)  

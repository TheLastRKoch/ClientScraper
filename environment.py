# Logs
LOG_FILE_PATH = "resources/client_scraper.log"

# Factura Electronica page
PAGE_COLUMN_LIST = [
    "Status",
    "ID",
    "Nombre",
    "Nombre comercial",
    "Telefono",
    "Cedula",
    "Fax",
    "Vencidos",
    "Sin vencer",
    "Con saldo",
    "Maximo D",
    "Contactos",
    "Direccion",
    "Rechazados",
    "Fact Ingles",
    "Estado",
    "Fact Mes",
    "Email",
    "Fact Automatica",
    "Impresion CABYS",
    "Cod Lista Precios",
    "Desc Lista Precios",
]

PAGE_LOGIN_TITLE = "La solución para su facturación electrónica"
PAGE_REQUEST_AUTH = "Please authenticate"
PAGE_FOLLOW_STEPS = "Please follow the next steps:\n- Go to the clients page\n- Select view all"
PAGE_PAGE_RANGE = "Please type the number of pages to extract [1-10]"
PAGE_HOMEPAGE_URL = r"https://facturatributaria.com"
PAGE_APP_URL = r"https://app.facturatributaria.com/Eos.wgx"
PAGE_XML_URL = r"https://app.facturatributaria.com/Route/2.1003048.4/kit/en-GB/CRF_TEMA/1048574.49148.926/0/CRF_TEMA/content.Eos.wgx?vwginstance=0"
PAGE_PAGING_ID = r"TRG_paging_100"

# Webdriver
SHOT_WAIT = 1
MEDIUM_WAIT = 3
LONG_WAIT = 5
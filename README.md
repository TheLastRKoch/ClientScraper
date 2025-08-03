# ClientScraper
Este proyecto es un web scraper diseñado para extraer datos de clientes desde [https://facturatributaria.com](https://facturatributaria.com/). La herramienta se desarrolló debido a que el equipo responsable de la plataforma discontinuará el servicio y no proporciona una forma sencilla de exportar la lista de clientes.

<br>

## Requisitos

Para utilizar este web scraper, se requiere lo siguiente:

- Python 3.11 o superior instalado.
- Credenciales válidas para [https://facturatributaria.com](https://facturatributaria.com/).

<br>

## Instrucciones de Uso

Siga estos pasos para ejecutar el web scraper:

1. **Crear un entorno virtual de Python**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar las rutas**:
   - Establezca la ruta para los archivos de registro (logs) y el directorio donde se guardarán los datos de los clientes en el archivo `environment.py`.

4. **Descargar la plantilla**:
   - Descargue el archivo `client_list.csv` y colóquelo en el directorio configurado para los datos de los clientes.

5. **Ejecutar el sistema**:
   ```
   python3 app.py
   ```

6. **Autenticación manual**:
   - El web scraper esperará a que inicie sesión manualmente en la plataforma. Presione Enter una vez autenticado.

7. **Navegar a la lista de clientes**:
   - Diríjase a la siguiente sección `CXC`>`Mantenimiento`>`Clientes`.

8. **Seleccionar opciones**:
   - En la barra de filtros, seleccione "Todos".
     <img width="341" height="35" alt="Screenshot from 2025-08-02 19-17-40" src="https://github.com/user-attachments/assets/344958f4-ce5f-4ce8-a96c-436ffa9ffd27" />

   - En la barra de registros, seleccione "Todas las líneas".
   <img width="341" height="73" alt="Screenshot from 2025-08-02 19-18-14" src="https://github.com/user-attachments/assets/6f34753d-d7fb-4d2c-b6dd-7a186845b140" />


9. **Verificar el número de páginas**:
   - Observe el número total de páginas mostrado en la lista de clientes.

10. **Ingresar el número de páginas**:
    - Ingrese el número total de páginas a extraer y presione Enter.

11. **Descarga de datos**:
    - El web scraper comenzará a descargar la lista de clientes.

<br>

## Notas

- Asegúrese de que las credenciales proporcionadas tengan acceso completo a la lista de clientes.
- Verifique que el archivo `client_list.csv` esté en el formato correcto para evitar errores durante la extracción.

# Proyecto MLOps de Predicción de Churn en Telecomunicaciones

Como parte de un proyecto del curso de **Machine Learning** de la **Universidad del Norte**, el mismo trata del uso de modelos de ML para la predicción de abandono de clientes (churn), construyendo una arquitectura básica de MLOps para implementar el modelo en un entorno de producción,utilizando herramientas como **Scikit-learn**, **FastAPI** y **Docker** para el entrenamiento y despliegue local, y un flujo de trabajo con **Github Actions** para validación del código en cada `push`.

### Autores del proyecto

- Johan Díaz

- Miguel Lugo 

- Luis Peñaranda

- Hector Sanjuan

### Componentes del proyecto
- `notebooks/`: Contiene el análisis exploratorio del dataset original y los cambios realizados al mismo. También se encuentra el entrenamiento y la evaluación de los modelos `Random Forest`, `XGBoost`, `CatBoost` y `LightGBM`, de los cuales se revisaron métricas como `roc_auc` y `recall` para la escogencia del mejor modelo. Cada notebook contiene interpretabilidad de resultados y uno de ellos incluye interpretabilidad por `LIME`.
- `app/api.py`: La API fue desarrollada con `FastAPI` y permite realizar predicciones sobre el abandono de clientes (churn) utilizando el mejor modelo conseguido, previamente entrenado y almacenado en `telco_churn_model.joblib`. A través del endpoint /predict, la API recibe los datos de un cliente, los procesa en un DataFrame de pandas y devuelve tanto la probabilidad de que el cliente registrado abandone el servicio y la clase predicha ("Yes" si sí abandona, "No" si no).
- `Dockerfile`: Una opción para el despliegue local de la **API** es usar el Dockerfile para construir una imagen reproducible y ejectuar el modelo sin dependencias externas.

- `Flujo de trabajo CI/CD con GitHub Actions`: Se configuró GitHub Actions para ejecutar automáticamente el linting con flake8 y las pruebas unitarias con pytest cada vez que se realiza un push.

### Instalación y ejecución de la **API**
```bash
pip install -r requirements.txt
uvicorn app.api:app --reload  # Desarrollo local
```

### Ejecución de la **API** usando docker
```bash
docker build -t telco-churn-api .
docker run -d --name telco-churn-container -p 8000:8000 telco-churn
```
Utilizamos los siguientes pasos para iniciar, detener y ver estado
```bash
docker start telco-churn-container
docker stop telco-churn-container
docker ps -a | grep telco-churn
```
Para cualquiera de los dos casos que decida ejecutar:

- Si desea acceder a la **API**, use el siguiente enlace en su navegador: http://127.0.0.1:8000/docs

- Si desea probar la **API**, acceda a /predict y use uno de los ejemplos que se detallan en el notebook `pruebas_prediccion_api.ipynb` en formato json.

- Si desea probar las predicciones directamente desde la terminal, en su computador abra el **símbolo del sistema (cmd)** y use el segundo formato especificado en el notebook ya mencionado.

## Ejemplo de ejecución de la **API**:


<p align="center">
  <img src="assets/churn-mlops.gif" width="600" alt="Vista previa de la API">
</p>



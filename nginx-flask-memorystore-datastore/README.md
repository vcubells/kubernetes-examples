# Ejemplo de una aplicación compuesta por Nginx + Flask + Cloud Memorystore + Cloud Datastore utilizando Kubernetes

En este ejemplo se muestra una aplicación compuesta por un proxy [Nginx](https://nginx.org/en/), una API desarrollada en [Flask](http://flask.pocoo.org/), una base de datos [Cloud Memorystore](https://cloud.google.com/memorystore/) para manejo de sesiones y una base de datos en [Cloud Datastore](https://cloud.google.com/datastore/) para el almacenamiento persistente de la información. La aplicación se despliega en un clúster de Kubernetes en [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). 


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Tener instalado `kubectl`. Mas información se encuentra disponible en [Install and Set Up kubectl
](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
* Tener una cuenta activa en [Google Cloud Platform](https://cloud.google.com/).
* Tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:

- [proxy-api.yaml](proxy-api.yaml): Archivo de configuración donde se definen los servicios a ejecutar dentro del clúster de Kubernetes.
- [app](app): Carpeta que contiene el código de la aplicación desarrollada en Flask.
- [config.py](app/config.py): Archivo de configuración de la aplicación.

## 3. Instrucciones de uso

### Creando un proyecto

1. Cree un proyecto en la [Consola de Google Cloud Platform](https://console.cloud.google.com). Póngale el nombre y ID que usted prefiera.

### Creando una instancia de Memorystore

2. Dentro de la consola, en el menú de la izquierda, seleccione la opción [Memorystore](https://console.cloud.google.com/memorystore/redis/instances) y dentro de esta **Crear instancia**.
3. Especifique el ID de la instancia, seleccione una región y zona, por ejemplo: `us-central1-b`.
4. Verifique que la opción **Red autorizada** aparezca con el valor *default* y seleccione el botón *Crear*.
5. Una vez que termine de crearse la instancia, ubique en la lista que aparece la *Dirección IP* y el *Número de puerto*. Guarde estos valores porque los utilizará posteriormente. 

### Creando una instancia de Datastore

6. Dentro de la consola, en el menú de la izquierda, seleccione la opción [Datastore](https://console.cloud.google.com/datastore/).
7. Ubique la opción titulada *Cloud Firestore en modo Datastore* y de clic en el botón *Seleccionar*.
8. Seleccione una región, de preferencia la misma o alguna cercana a la misma zona utilizada al crear la instancia de Memorystore.
9. Seleccione la opción *CREAR BASE DE DATOS*.

### Creando el clúster de Kubernetes

10. Dentro de la misma consola, en el menú de la izquierda, seleccione la opción [Kubernetes Engine / Clústeres de Kubernetes](https://console.cloud.google.com/kubernetes) y cree un nuevo clúster dentro del mismo proyecto.
11. Cambie el nombre del clúster y la zona. Asegúrese de seleccionar la misma región y zona que escogió al crear la instancia de Memorystore. En este caso por ejemplo: `us-central1-b`.
12. En el **Grupo de nodos** seleccione el botón *Edición avanzada* y desplácese hacia abajo. Asegúrese de seleccionar en **Alcance de acceso** la opción *Permitir el acceso completo a todas las API de Cloud* y seleccione el botón *Guardar*.
13. Seleccione la opción **Opciones avanzadas** y localice la sección **Redes**. Seleccione la casilla *Habilitar la VPC nativa (mediante una IP de alias)* y deje la opción **Red** en el valor *default*.
Los demás valores déjelos como aparecen de manera predeterminada.
14. Una vez creado el clúster, seleccione la opción "Conectar" y en la ventana que aparece, seleccione el primer comando relacionado con `kubectl`. El comando a copiar tiene una estructura similar a la siguiente:

`gcloud container clusters get-credentials cluster-vcn --zone us-central1-b --project cloudtpu-vcn`

15. Ejecute el comando anterior en una terminal de su computadora.

### Configurando y desplegando la aplicación

16. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
17. Cámbiese a la carpeta del proyecto.
18. Edite el archivo [config.py](app/config.py) y sustituya los valores `REDIS_HOST`, `REDIS_PORT` y `PROJECT_ID` por los que les corresponden. Los valores de Redis son los que obtuvo al crear la instancia de Memorystore. El valor de `PROJECT_ID es el que aparece en el parámetro `--project` del comando ejecutado previamente. Guarde todos los cambios realizados.
19. Compile la imagen del contenedor con el siguiente comando. No olvide sustituir `<PROJECT ID>` por el valor correcto.

`docker build -t gcr.io/<PROJECT ID>/flask-api app/.`

20. Suba la imagen del contendor al registro de su proyecto en Google Cloud Platform. No olvide sustituir `<PROJECT ID>` por el valor correcto.

`docker push gcr.io/<PROJECT ID>/flask-api`

21. Despliegue la aplicación en Google Cloud Platform:

`kubectl apply -f proxy-api.yaml`

22. Verifique que los servicios se encuentran funcionando correctamente:

`kubectl get deployment`

`kubectl get service`

`kubectl get pod`

23. Obtenga la URL del servicio. Ejecute varias veces este comando hasta que el valor `EXTERNAL-IP` se encuentre asignado:

`kubectl get service`

24. Acceda a la aplicación en un browser con la IP externa obtenida en el paso anterior.


## 4. Liberando los recursos
 
25. Para eliminar la aplicación y los servicios creados ejecute:

`kubectl delete  -f proxy-api.yaml`

26. Desde la [Consola de Google Cloud Platform](https://console.cloud.google.com), elimine el clúster de Kubernetes.
27. Porteriormente, elimine la instancia de Memorystore.
28. Por último, elimine el proyecto.


## 5. Recursos

Para conocer más sobre Memorystore consulte la documentación oficinal disponible en [Cloud Memorystore](https://cloud.google.com/memorystore/).

Para conocer más sobre Datastore consulte la documentación oficinal disponible en [Cloud Datastore](https://cloud.google.com/datastore/).

Para conocer más sobre Kubernetes Engine consulte la documentación oficial disponible en  [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/).

Para conocer más sobre Kubernetes consulte la documentación oficial disponible en  [Kubernetes](https://kubernetes.io).

Para aprender a trabajar con el comando `kubectl`consulte la documentación oficial disponible en [Install and Set Up kubectl
](
https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Para conocer más sobre Google Cloud Platform consulte la documentación oficial disponible en  [GCP Documentation](https://cloud.google.com/docs/).
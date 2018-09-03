# Ejemplo de una aplicación compuesta por Nginx + Flask + Redis + MongoDB utilizando Kubernetes

En este ejemplo se muestra una aplicación compuesta por un proxy [Nginx](https://nginx.org/en/), una API desarrollada en [Flask](http://flask.pocoo.org/), una base de datos [Redis](https://redis.io/) para manejo de sesiones y una base de datos en [MongoDB](https://www.mongodb.com/) para el almacenamiento persistente de la información. La aplicación se despliega en un clúster de Kubernetes en [Google Cloud Platform](https://cloud.google.com/). 

Para Redis y MongoDB se utilizan servicios en la nube ofrecidos por [Redis Labs](https://redislabs.com/) y [mLab](https://mlab.com/) respectivamente.

## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Tener instalado `kubectl`. Mas información se encuentra disponible en [Install and Set Up kubectl
](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
* Tener una cuenta activa en [Google Cloud Platform](https://cloud.google.com/).
* Tener una cuenta activa en Redis Labs o utilizar un servidor Redis local. Puede crear una cuenta gratuita [aquí](https://app.redislabs.com/#/sign-up/cloud).
* Tener una cuenta activa en [mLab](https://mlab.com/) o utilizar un servidor de MongoDB local. Puede crear una cuenta gratuita [aquí](https://mlab.com/signup/).
* Tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:

- [proxy-api.yaml](proxy-api.yaml): Archivo de configuración donde se definen los servicios a ejecutar dentro del clúster de Kubernetes.
- [app](app): Carpeta que contiene el código de la aplicación desarrollada en Flask.
- [config.py](app/config.py): Archivo de configuración de la aplicación.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree un proyecto en la [Consola de Google Cloud Platform](https://console.cloud.google.com). Póngale el nombre y ID que usted prefiera.
4. Dentro de la misma consola, en el menú de la izquierda seleccione la opción Kubernetes Engine / Clústeres de Kubernetes  y cree un nuevo clúster dentro del proyecto creado en el paso anterior.
5. Cambie el nombre nombre del clúster, la versión del clúster a la 1.9.4-gke.1 y el tamaño del clúster a 1 nodo. Los demás valores déjelos como aparecen de manera predeterminada.
6. Una vez creado el clúster, seleccione la opción "Ejecutar" y en la ventana que aparece, seleccione el primer comando relacionado con `kubectl`. El comando a copiar tiene una estructura similar a la siguiente:

`gcloud container clusters get-credentials demo-webinar --zone us-central1-a --project webinar-199317`

7. Ejecute el comando anterior en una terminal de su computadora.
8. Compile la imagen del contenedor de la aplicación, sustituyendo `<PROJECT ID>` por el que le correponde. Este valor es el que aparece en el parámetro `--project` del comando ejecutado en el paso anterior:

`docker build -t gcr.io/<PROJECT ID>/flask-api app/.`

9. Suba la imagen del contendor al registro de su proyecto en Google Cloud Platform:

`gcloud docker -- push gcr.io/<PROJECT ID>/flask-api`

10. Despliegue la aplicación en Google Cloud Platform:

`kubectl create -f proxy-api.yaml`

11. Verifique que los servicios se encuentran funcionando correctamente:

`kubectl get deployment`
`kubectl get service`
`kubectl get pod`

12. Obtenga la URL del servicio. Ejecute varias veces este comando hasta que el valor EXTERNAL-IP se encuentre asignado:

`kubectl get service`

13. Acceda a la aplicación en un browser con la IP externa obtenida en el paso anterior.

14. Para eliminar la aplicación y los servicios creados ejecute:

`kubectl delete  -f proxy-api.yaml`

15. Elimine el clúster desde la [Consola de Google Cloud Platform](https://console.cloud.google.com).


## 4. Recursos

Para conocer más sobre Kubernetes consulte la documentación oficial disponible en  [Kubernetes](https://kubernetes.io).

Para aprender a trabajar con el comando `kubectl`consulte la documentación oficial disponible en [Install and Set Up kubectl
](
https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Para conocer más sobre Google Cloud Platform consulte la documentación oficial disponible en  [GCP Documentation](https://cloud.google.com/docs/).
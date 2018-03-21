# Ejemplo de una aplicación compuesta por Nginx + Flask + Redis + MongoDB utilizando Kubernetes

En este ejemplo se muestra una aplicación compuesta por cuatro microservicios: un proxy [Nginx](https://nginx.org/en/), una API desarrollada en [Flask](http://flask.pocoo.org/), una base de datos [Redis](https://redis.io/) para manejo de sesiones y una base de datos en [MongoDB](https://www.mongodb.com/) para el almacenamiento persistente de la información. La aplicación se despliega en un clúster local de Kubernetes utilizando `minikube`. Cada servicio se ejecuta en su propio contenedor, y estos, se encuentran enlazados entre sí. 

## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Tener instalado `minikube`. Le recomiendo consultar el documento [Kubernetes on MacOS with Minikube](https://docs.google.com/document/d/1KYlbHYI7gz-Hwe_f_m6Nw6aQxK5rCpeXCJDz6EGeO54/edit?usp=sharing) en el cual explico paso a paso cómo configurar el entorno de desarrollo y cómo trabajar con diferentes opciones de [Minikube](https://github.com/kubernetes/minikube).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:



## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Verifique que `minikube`se encuentra en ejecución con el comando:

`minikube status`

o si requiere iniciarlo, ejecute el comando:

`minikube start`

4. Ejecute el comando:

`kubectl create -f `

5. Verifique que los servicios se encuentran funcionando correctamente:

`kubectl get deployment`
`kubectl get service`
`kubectl get pod`

6. Obtenga la URL del servicio :

`minikube service <service> --url`

7. Acceda a la interfaz web de la aplicación en un browser con la URL obtenida en el paso anterior, o también lo puede hacer directamente desde la terminal con el comando:

`open $(minikube service <service> --url)`

8. Para eliminar los contenedores y los servicios creados:

`kubectl delete  -f `

9. Para detener `minikube`:

`minikube stop` 

## 4. Recursos


Para conocer las diferentes opciones de minikube, así como instalar y configurar el entorno de desarrollo, consulte la guía [Kubernetes on MacOS with Minikube](https://docs.google.com/document/d/1KYlbHYI7gz-Hwe_f_m6Nw6aQxK5rCpeXCJDz6EGeO54/edit?usp=sharing).

Para conocer más sobre Minikube consulte la documentación oficial disponible en  [Minikube](https://github.com/kubernetes/minikube).

Para conocer más sobre Kubernetes consulte la documentación oficial disponible en  [Kubernetes](https://kubernetes.io).

Para aprender a trabajar con el comando `kubectl`consulte la documentación oficial disponible en [Install and Set Up kubectl
](
https://kubernetes.io/docs/tasks/tools/install-kubectl/).
# Ejemplo de Celery

## Cómo instalarlo

    Necesitaremos crear un entorno virtual, e instalar las librerías necesarias:

    - pip3 install -r requirements.txt

    Así mismo, necesitamos un servidor de redis corriendo. 

## Cómo ejecutarlo
 
    1. Necesario tener el redis corriendo: redis-server
    2. Se pueden desplegar de manera independiente:

    - Ejecutar la cola de menor prioridad: celery -A main:celery worker -Q low_priority -l debug
    - Ejecutar la cola de mayor prioridad: celery -A main:celery worker -Q high_priority -l debug
    - Ejecutar el celery beat: celery -A main:celery beat -l debug
    - Ejecutar el celery flower: celery -A main:celery flower 
    - Ejecutar el servidor: python3 -m uvicorn main:app --reload

## Que está configurado

Actualmente, hay dos tareas que se ejecutan cada 30 segundos. 
Además, una de ellas se puede lanzar a través de una API de manera directa,
y otra con un delay.





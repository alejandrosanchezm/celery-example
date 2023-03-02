celery -A tasks worker -Q low_priority -l debug
celery -A tasks worker -Q high_priority -l debug
celery -A tasks beat -l debug
celery -A tasks flower 
python3 -m uvicorn main:app --reload
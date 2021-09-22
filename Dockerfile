FROM python:3.6.1-alpine
WORKDIR /GroceryStore
ADD . /GroceryStore
RUN pip install -r requirements.txt
CMD ["python","app.py"]
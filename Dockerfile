FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

RUN python3 -m pip install --force-reinstall pastebin-0.0.1-py2.py3-none-any.whl

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=8882"]
CMD [ "python3", "-m" , "flask", "run","--port=8882"]


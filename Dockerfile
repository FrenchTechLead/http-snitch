FROM python:alpine3.17
COPY snitch.py snitch.py
RUN pip install colorama
EXPOSE 8080
ENTRYPOINT ["python3", "-u" ,"snitch.py"]
FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 2375
ENTRYPOINT ["python"]
CMD ["app.py"]

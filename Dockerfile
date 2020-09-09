FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 2375
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0 --port=2375"]

FROM python:3.7.4

LABEL maintainer "Aleksandra Maciaga"
LABEL image_type "Flask web service"

ENV DOC_ROOT /app

WORKDIR ${DOC_ROOT}

COPY webApp .

RUN pip install --upgrade pip && \
pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
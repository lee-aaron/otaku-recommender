FROM gcr.io/google-appengine/python
LABEL python_version=python2.7
RUN virtualenv --no-download /env -p python2.7

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install numpy
RUN pip install -r requirements.txt
ADD . /app/
CMD exec gunicorn -b :$PORT main:app

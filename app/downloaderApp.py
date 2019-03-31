from celery import Celery
import urllib.request


# Where the downloaded files will be stored
BASEDIR = "/Users/ana/PycharmProjects/coursepy/app/templates/user.html"

# Create the app and set the broker location (RabbitMQ)
app = Celery('Pogoda',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')


@app.task
def upload_pogoda(url, filename):
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASEDIR + "/" + filename, 'wb') as file:
        file.write(data)
    file.close()


@app.task
def list():
    """ Return an array of all downloaded files """
    return


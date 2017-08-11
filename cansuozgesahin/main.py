import webapp2
import os #added

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.render('index.html', values)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

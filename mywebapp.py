import jinja2
import webapp2
import os
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CommentEntry(ndb.Model):
    """A main model for representing an individual Comment entry."""
    username = ndb.StringProperty(indexed=False)
    comment = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        comments = CommentEntry.query().order(-CommentEntry.date).fetch(20)
        template_values = {
            'comments': comments
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        username_entered = self.request.get('username')
        comment_entered = self.request.get('comment')
        if self.valid_username(username_entered) and self.valid_comment(comment_entered):
            entry = CommentEntry(username = username_entered, comment = comment_entered)
            entry.put()
            self.redirect('/')
        else:
            template_values = {
                'error': 'Username or comment are not valid!',
                'username': username_entered,
                'comment': comment_entered
            }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))

    def valid_username(self, s):
        m = len(s)
        if m > 1 and m < 15:
            return True
        else:
            return False

    def valid_comment(self, s):
        m = len(s)
        if m > 5 and m < 1000:
            return True
        else:
            return False




app = webapp2.WSGIApplication([
    ('/', MainPage),    
], debug=True)

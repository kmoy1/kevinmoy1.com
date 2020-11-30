from flask_misaka import Misaka, markdown
from misaka import Markdown, HtmlRenderer
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

from flask import Flask, render_template, request
# from flaskext.markdown import Markdown
from app import app, render_template, request

class HighlighterRenderer(HtmlRenderer):
   def blockcode(self, text, lang):
      try:
         lexer = get_lexer_by_name(lang, stripall=True)
      except ClassNotFound:
         lexer = None

      if lexer:
         formatter = HtmlFormatter()
         return highlight(text, lexer, formatter)
      # default
      return '\n<pre><code>{}</code></pre>\n'.format(text)

Misaka(app)

@app.route('/test')
def test():
   md_file = open("static/notes-md/test.md", "r").read()
   return render_template('test.html', md_file = markdown(md_file, fenced_code=True, math=True, math_explicit=True))

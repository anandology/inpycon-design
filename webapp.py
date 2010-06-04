import web

urls = (
    "/(themes/.*)", "media",
    "/(.*)", "page"
)
app = web.application(urls, globals())

tglobals = dict(
    ctx=web.storage(
        user=None, 
        flash_messages=[], 
    ),
    homepath=lambda: "",
    get_flash_messages=lambda: [],
)

text = """
<p>PyCon India 2010 is the second Python conference in India. A purely volunteer effort, it is being hosted for the second time in India, and will attract some of the best Python developers in India and abroad.
</p>

<h2>Venue</h2>
<p>M S Ramaiah Institute of Technology    <br />

   Bangalore
</p>

<h2>Dates to Remember</h2>
<p>The conference will take place on 25th and 26th, September 2010. The calendar will be posted soon.
</p>

<h2>About</h2>
<p>The conference will consist of a number of full length presentations, a number of shorter lightning talks and open sprints and BoFs.
</p>

<h2>Staying upto date</h2>
<p>Please subscribe to <a href="http://in.pycon.org/2010/feed">RSS feed</a> to stay up-to-date on the changes to the site
</p>

<h3>Testing H3</h3>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<h4>Testing H4</h4>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

def render_page(name):
    name = name or "PyCon India 2010"
    return web.template.TemplateResult(title=name, __body__=text)

class media:
    def GET(self, path):
        raise web.found("/static/" + path)

class page:
    def GET(self, name):
        i = web.input(theme="alankar")
        t = web.template.frender("static/themes/" + i.theme + "/site.html", globals=tglobals)
        return t(render_page(name))

if __name__ == "__main__":
    app.run()

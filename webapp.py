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
<h2>Welcome</h2>

<p>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
"""

def render_page(name):
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

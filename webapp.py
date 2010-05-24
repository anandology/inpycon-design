import web

urls = (
    "/(themes/.*)", "media",
    "/(.*)", "page"
)
app = web.application(urls, globals())

tglobals = dict(
    ctx=web.storage(user=None, flash_messages=[]),
    homepath=lambda: "",
)

def render_page(name):
    return web.template.TemplateResult(title=name, __body__="Hello, world!")

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

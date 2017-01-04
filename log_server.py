from klein import run, route
from twisted.web.static import File
from twisted.web.template import Element, renderer, FilePath, XMLFile

from logs import LogHandler


class Messages(Element):
    loader = XMLFile(FilePath('templates/logs.html'))

    def __init__(self):
        self.lh = LogHandler('tests')
        self.messages = self.lh.get_messages()

    @renderer
    def log_messages(self, request, tag):
        for m in self.messages:
            yield tag.clone().fillSlots(
                log_time=m.time,
                log_nick=m.nick,
                log_message=m.message
            )


# Routing:

@route('/static/', branch=True)
def static(request):
    return File("./static")


@route('/')
def home(request):
    return Messages()


run("localhost", 8080)

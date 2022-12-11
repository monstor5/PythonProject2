import eel

eel.init("Web")


@eel.expose
def call_in_js(x):
    print(x)


eel.start("index.html", size = (500, 500))
"""Generate UI elements via jinja2 to display on page load."""
# This file will fail linting generally as await calls are not supposed to be run on a main thread
# However this file is loaded as an async call by javascript so while python linters complain the file is valid
import js
from js import document
import micropip
from jinja2 import Environment, FunctionLoader
from pyodide import to_js
import json

await micropip.install("pyodide-importer")  # type: ignore  # noqa
from pyodide_importer import register_hook  # type: ignore  # noqa

register_hook("/")
js.listeners = []
js.progression_presets = []
js.background_worker = None


def ajax_call(file):
    resp = js.jquery.ajax(js.Object.fromEntries(to_js({"type": "GET", "url": file, "async": False}))).responseText
    return resp


def loader_func(template_name):
    return ajax_call("templates/" + template_name)


for file in json.loads(ajax_call("static/presets/preset_files.json")).get("progression"):
    js.progression_presets.append(json.loads(ajax_call("static/presets/" + file)))

templateEnv = Environment(loader=FunctionLoader(loader_func), enable_async=True)
template = templateEnv.get_template("base.html.jinja2")
rendered = await template.render()  # type: ignore  # noqa
js.document.documentElement.innerHTML = ""
js.document.open()
js.document.write(rendered)
js.document.close()


# Load settings from the cookies if it exists
cookie_data = document.cookie
if cookie_data:
    for cookie in cookie_data.split(";"):
        if "settings=" in cookie:
            settings_cookie = str(cookie).replace("settings=", "")
            break
    json_data = json.loads(settings_cookie)
    for key in json_data:
        try:
            # TODO: Validate this still works now that we switched engines
            document.getElementById(key).value = json_data[key]
        except Exception:
            pass

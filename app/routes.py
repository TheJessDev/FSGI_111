from flask import Flask  # from the flask module import the Flask class
# PEP 8, style guide...snake_case

app = Flask (__name__)   # create an instance of Flask (object) into our variable "app"
                            #fromm here on out, "app" is now an "object", object is to class (of atrubutes and) as house is to blueprint

@app.get("/")     # we can now use our objects method to "GET" as a decorator.
def index():     # a decorator ( @ ) wraps a function ( view function), creates a map
    me = {         # on this line . we create a new directory with key/value pairs
        "first_name": "Jess",  # "key": "value",
        "last_name": "Mor",
        "hobbies": "trading",
        "is_active": True
    }
    return me       # when you return a directory from a view function,
                    # flask automatically converts it to JSON for compatability (JavaScript Object Notation)

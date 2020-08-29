import web

# urls = ('/', 'index')
urls = ('/jackass', 'index')

app = web.application(urls, globals())

# render = web.template.render('templates/')
render = web.template.render('templates/', base="layout")

class index(object):
    def GET(self):
        # mygreeting = "Hello World!"
        # return mygreeting

        # Instead of just a string for greeting I'm now using web.input to get data from the browser. This function takes a key=value set of defaults, parses the ?name=Frank part of the URL you give it, and then returns a nice object for you to work with that represents those values.
        # I then construct the greeting from the new form.name attribute of the form object, which should be very familiar to you by now.
        # form = web.input(name="Nobody", jabroni=None)
        # mygreeting = "Hello %s " % (form.name)

        # if form.jabroni:
        #     mygreeting = "Hello %s, %s" % (form.jabroni, form.name)
        #     return render.index(greeting=mygreeting)
        # else:
        #     return "ERROR: jabroni is required"

        # Form handling
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", jabroni="bazoomba")
        mygreeting = "Hello %s %s" % (form.name, form.jabroni)
        return render.index(greeting=mygreeting)


if __name__ == '__main__':
    app.run()

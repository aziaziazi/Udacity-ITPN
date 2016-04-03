 # Lession 4.6: Responding Based on Verification

# This session will show us how we can put in custom responses in our server in order to respond
# to a user whether the birthday entered is valid or not

# https://www.udacity.com/course/viewer#!/c-nd000/l-4175328805/m-48714318


import webapp2
import valid_date

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month" value="%(month)s">
    </label>

    <label> Day
        <input type="text" name="day" value="%(day)s">
    </label>

    <label> Year
        <input type="text" name="year" value="%(year)s">
    </label>

    <div style="color:red">%(error)s</div>

    <br>
    <br>
    <input type="submit">
</form>
"""




class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error" : error,
                                        "month" : month,
                                        "day" : day,
                                        "year" : year})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = valid_date.valid_month(user_month)
        day = valid_date.valid_day(user_day)
        year = valid_date.valid_year(user_year)

        if (month and day and year):
            self.response.out.write("Thanks beeing so good at selecting dates!")
        else:
            self.write_form("That's not valid to me, my friend", user_month, user_day, user_year)

app = webapp2.WSGIApplication([("/", MainPage)], debug = True)

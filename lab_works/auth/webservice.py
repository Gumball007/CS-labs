from flask import *
from flask_bootstrap import Bootstrap
import pyotp

# configuring flask application
webserver = Flask(__name__)
webserver.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(webserver)

### implements a basic authentication

@webserver.route('/login/')
def login():
    return render_template('login.html')


@webserver.route('/login/', methods=['POST'])
def login_form():
    # demo creds
    creds = {"username": "ana", "password": "12345678"}

    # getting form data
    username = request.form.get("username")
    password = request.form.get("password")

    # authenticating submitted creds with demo creds
    if username == creds["username"] and password == creds["password"]:
        # inform users if creds are valid
        flash("The credentials provided are valid", "success")
        return redirect(url_for("login_2fa"))
    else:
        # inform users if creds are invalid
        flash("You have supplied invalid login credentials!", "danger")
        return redirect(url_for("login"))


### implements 2FA authentication

# 2FA page route
@webserver.route("/login/2fa/")
def login_2fa():

    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("login_2fa.html", secret=secret)

# 2FA form route
@webserver.route("/login/2fa/", methods=["POST"])
def login_2fa_form():
    # getting secret key used by user
    secret = request.form.get("secret")
    # getting OTP provided by user
    otp = int(request.form.get("otp"))

    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("login_2fa"))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))


# running flask server
if __name__ == "__main__":
    webserver.run(debug=True)

# Defines the function and lets it know to expect 2 arguements
def is_valid(username, password):
    # Write code here
    # Defines what the users password should be
    valid_user_password = "qweasd"
    # if statement to check if the username matches admin but with no checks on the password
    if username == "admin":
        return True
    # if statement to check if the username and password match our requirements
    if username == "user" and password == valid_user_password:
        return True
    # else statement to catch anything else
    else:
        return False
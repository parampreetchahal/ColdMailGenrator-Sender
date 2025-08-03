def mask_email(email):
    user, domain = email.split("@")
    masked_user = user[0] + "*"*(len(user)-2) + user[-1] if len(user) > 2 else user
    return f"{masked_user}@{domain}"

def mask_name(name):
    return name[0] + "*"*(len(name)-1) if len(name) > 1 else name

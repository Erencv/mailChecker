def generate_email_combinations(first_name, last_name, domain):
    patterns = [
        '{first}@{domain}',
        '{first}.{last}@{domain}',
        '{first}{last}@{domain}',
        '{f}.{last}@{domain}',
        '{f}{last}@{domain}',
        '{last}.{first}@{domain}',
        '{first}_{last}@{domain}',
        '{last}@{domain}',
    ]
    first = first_name.lower()
    last = last_name.lower()
    f = first[0]
    for pattern in patterns:
        yield pattern.format(first=first, last=last, f=f, domain=domain)

# def verify_email_smtp(email):
#     try:
#         domain = email.split('@')[1]
#         records = dns.resolver.resolve(domain, 'MX')
#         mxRecord = str(records[0].exchange)
#         server = smtplib.SMTP(mxRecord)

#         server.set_debuglevel(0)
#         server.ehlo()
#         server.mail('me@mydomain.com')
#         code, message = server.rcpt(str(email))
#         server.quit()

#         if code == 250:
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(f"Error verifying {email}: {e}")
#         return False


# for email in generate_email_combinations(first_name, last_name, domain):
#     if verify_email_smtp(email):
#         valid_emails.append(email)
#         print(f"Valid email found: {email}")

# print(f"All valid emails: {valid_emails}")


# for email in generate_email_combinations(first_name, last_name, domain):
#     if validate_email(email, verify=True):
#         valid_emails.append(email)
#         print(f"Valid email found: {email}")
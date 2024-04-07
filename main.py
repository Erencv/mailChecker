import socket
import smtplib
import dns.resolver

try:
    records = dns.resolver.resolve('leanscale.com', 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    print(mxRecord)

    host = socket.gethostname()
    server = smtplib.SMTP_SSL(mxRecord, port=465, timeout=10)
    server.set_debuglevel(1)
    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code, message = server.rcpt(str("eren.cavus@leanscale.com"))
    server.quit()

    print(code)
    print(message)
    if code == 250:
        print('Success')
    else:
        print('Bad')
except Exception as e:
    print(f"Error verifying: {e}")
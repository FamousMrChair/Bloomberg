while 1:
    alert = False
    send = ""
    blacklist = []
    import EmailProgram
    for i in stockstosend:
        if i not in blacklist:
            send = send + i + ","
            blacklist = blacklist.append(i)
            alert = True

    #sending email

    sender_email = "cryptoprogramming0@gmail.com"
    receiver_email = "theclassroomnerdxd@gmail.com"
    password = 'FamousMrChair$()'
    message = MIMEMultipart("alternative")
    message["Subject"] = "crypto trading"
    message["From"] = sender_email
    message["To"] = receiver_email
    html = """
    <html>
    <body>
        <p>This message was sent using Python!<br>
        Let's get ready for some epic stock analysis</br>
        <br>Stocks that are trending in the US: """ """+ stockstosend + """ """</br>
        </p>
    </body>
    </html>
    """

    part2 = MIMEText(html, "html")
    message.attach(part2)

    context = ssl.create_default_context()
    if alert == True:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    # Sending messages
    sms_gateway = '9292152018@txt.att.net'
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(sender_email,password)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = sms_gateway
    msg['Subject'] = "Stocks"
    body = "This message was sent with python!"
    msg.attach(MIMEText(body,'plain'))

    if alert == True:
        sms = msg.as_string()
        server.sendmail(sender_email,sms_gateway,sms)
        server.quit()
    time.sleep(30)
    os.system("python3 emailprogram.py")

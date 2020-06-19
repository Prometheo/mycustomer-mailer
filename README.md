# mycustomer-mailer
an email reminder microservice
this restful api takes in the mailing details and sends a mail with the sites domain as the mail sender,
Provide the mailing details as follows: 
1. {
      "subject": "title of the message goes here",
      "body": "content/message",
      "mail_to": [a list of email address of the recipients],
}

for now the sender's email is my personal email, but once we have a registered email for the app, i will swap it in.

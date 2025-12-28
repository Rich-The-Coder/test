from datetime import date
import smtplib
from email.mime.text import MIMEText

# ========= CONFIGURE THESE =========
OUTLOOK_EMAIL = "your_outlook_email@outlook.com"
OUTLOOK_PASSWORD = "your_outlook_password_or_app_password"

# Where to send the email reminder
TO_EMAIL = "your_outlook_email@outlook.com"

# T-Mobile text via email-to-SMS gateway
# Replace with your 10-digit number, no dashes:
# Example: "8135551234@tmomail.net"
SMS_EMAIL = "YOURNUMBER@tmomail.net"

# All reminder dates (year, month, day)
# We’ll cover BOTH rumored ticket dates:
# - Jan 21, 2026 (widely posted on socials)
# - Feb 26, 2026 (mentioned on an event-planning site)
REMINDER_MESSAGES = {
    date(2026, 1, 14): "One week until the FIRST rumored Ulta Beauty World 2026 ticket drop (Jan 21). Check Ulta's site & Instagram today.",
    date(2026, 1, 21): "TODAY is the FIRST rumored Ulta Beauty World 2026 ticket drop (Jan 21). Go buy tickets ASAP.",
    date(2026, 2, 19): "One week until the BACKUP possible Ulta Beauty World 2026 ticket date (Feb 26). Double-check Ulta's announcements.",
    date(2026, 2, 26): "BACKUP possible Ulta Beauty World 2026 ticket drop is TODAY (Feb 26). Check for tickets now."
}

EMAIL_SUBJECT = "Ulta Beauty World 2026 Tickets Reminder"

# ========= END OF CONFIG =========

def send_email(subject: str, body: str, recipients: list[str]) -> None:
    """Send an email (and SMS via email) using Outlook SMTP."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = OUTLOOK_EMAIL
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
        server.sendmail(OUTLOOK_EMAIL, recipients, msg.as_string())


def main() -> None:
    today = date.today()
    print(f"Today is {today.isoformat()}")

    if today in REMINDER_MESSAGES:
        body = REMINDER_MESSAGES[today] + (
            "\n\nEvent details:\n"
            "Ulta Beauty World 2026\n"
            "Orlando, FL – April 16, 2026\n"
            "DON'T WAIT – tickets can sell out fast."
        )
        recipients = [TO_EMAIL, SMS_EMAIL]

        try:
            send_email(EMAIL_SUBJECT, body, recipients)
            print("Reminder sent by email and text.")
        except Exception as e:
            print(f"Error sending reminder: {e}")
    else:
        print("No Ulta reminder scheduled for today.")


if __name__ == "__main__":
    main()
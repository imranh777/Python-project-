#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        """ """
        pass

    # FA.3
    # 
    def del_email(self, m_id):
        """  """
        pass

    # FA.4
    # 
    def filter(self, frm):
        """  """
        pass

    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    def show_emails(self):
        print(f"{'ID':<4} {'From':<25} {'To':<25} {'Date':<12} {'Subject':<15} {'Tag':<8} Body")

        for email in self._mailbox:
            print(f"{email.m_id:<4} {email.frm:<25} {email.to:<25} {email.date:<12} "
                  f"{email.subject:<15} {email.tag:<8} {email.body}")

    # FB.2
    # 
    def mv_email(self, m_id, tag):
            for email in self._mailbox:
                if email.m_id == m_id:
                    email.tag = tag
                    return email
            return None

    # FB.3
    # 
    def mark(self, m_id, m_type):
        for email in self._mailbox:
            if email.m_id == m_id:
                if m_type == "read":
                    email.read = True
                elif m_type == "flag":
                    email.flag = True
                return email
        return None

    # FB.4
    # 
    def find(self, date):
        results = []
        for email in self._mailbox:
            if email.date == date:
                results.append(email)
        return results

    # FB.6
    #
    def add_email(self, frm, to, date, subject, tag, body):
        # 1. Generate unique ID based on current number of emails
        m_id = len(self._mailbox) + 1

        # 2. Create the correct email type based on tag
        if tag == "conf":
            email = Confidential(m_id, frm, to, date, subject, tag, body)
        elif tag == "prsnl":
            email = Personal(m_id, frm, to, date, subject, tag, body)
        else:
            email = Mail(m_id, frm, to, date, subject, tag, body)

        # 3. Assign ID to email
        email.m_id = m_id

        # 4. Add the new email to the mailbox
        self._mailbox.append(email)

        # 5. Return the email so the interpreter can display it
        return email

    







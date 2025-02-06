"""1517. Find Users With Valid E-Mails

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 

Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'.
The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # import string
    # def allowed_mail(mail: str) -> bool:
    #    allowed_chars = string.ascii_letters + string.digits + "_.-"
    #    mail_split = mail.split("@")
    #    if len(mail_split) != 2:
    #        return False
    #    prefix_cond = mail_split[0].isalpha() and all(
    #        char in allowed_chars for char in mail_split[0][1:]
    #    )
    #    domain_cond = mail_split[1] == "leetcode.com"
    #    return prefix_cond and domain_cond
    # return users[users["mail"].apply(allowed_mail)]
    return users[users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9\_\.\-]*@leetcode\.com$")]

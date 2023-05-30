import re  
import smtplib  
from datetime import datetime  
import time  

from email.mime.multipart import (
    MIMEMultipart,
)  # Imports Multipurpose Internet Mail Extensions
from email.mime.text import (
    MIMEText,
)  # Sub-class of MineMase used for adding text to email
from email.mime.base import (
    MIMEBase,
)  # Base class for all MIME-specific subclasses in email

from email import (
    encoders,
)  # Module with functions to encode & decode data in various formats
from email.mime.application import (
    MIMEApplication,
)  # Adds non-text files to email messages

from config import mail_credentials  # custom module for storing email credentials

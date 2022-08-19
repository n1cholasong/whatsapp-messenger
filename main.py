from dotenv import load_dotenv
import pywhatkit as w
import datetime
import os

load_dotenv()

phone_list = [os.environ.get("phone-no")]
# phone_dict = {"NAME": 12345678}

link = "link"

msg = "Hello, this is Nicholas from Makers Innovators Tribe (M.I.T), could you help me to fill up this membership form. Thanks.\n\n" \
      f"{link}" \

# List
for number in phone_list:
    now = datetime.datetime.now()
    w.sendwhatmsg("+65" + str(number), msg, now.hour, now.minute + 1, 7, True, 2)
    print(f"Message Sent to {number}!")

# Dictionary
# for name, number in phone_dict.items():
#     now = datetime.datetime.now()
#     w.sendwhatmsg("+65" + str(number), msg, now.hour, now.minute + 1, 7, True, 2)
#     print(f"Message Sent to {name}!")

import pyfiglet

title=pyfiglet.figlet_format("Password complexity checker", justify='center')
print(title, end="")

def time_to_crack_password(password):
    # Lookup table for time to crack based on password length and complexity
    time_lookup = {
        4: {"Numbers Only": "Instantly", "Lowercase Letters": "Instantly", "Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters, Symbols": "Instantly"},
        5: {"Numbers Only": "Instantly", "Lowercase Letters": "Instantly", "Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters, Symbols": "Instantly"},
        6: {"Numbers Only": "Instantly", "Lowercase Letters": "Instantly", "Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters": "Instantly", "Numbers, Upper and Lowercase Letters, Symbols": "Instantly"},
        7: {"Numbers Only": "Instantly", "Lowercase Letters": "Instantly", "Upper and Lowercase Letters": "1 sec", "Numbers, Upper and Lowercase Letters": "2 secs", "Numbers, Upper and Lowercase Letters, Symbols": "4 secs"},
        8: {"Numbers Only": "Instantly", "Lowercase Letters": "Instantly", "Upper and Lowercase Letters": "28 secs", "Numbers, Upper and Lowercase Letters": "2 mins", "Numbers, Upper and Lowercase Letters, Symbols": "5 mins"},
        9: {"Numbers Only": "Instantly", "Lowercase Letters": "3 secs", "Upper and Lowercase Letters": "24 mins", "Numbers, Upper and Lowercase Letters": "2 hours", "Numbers, Upper and Lowercase Letters, Symbols": "6 hours"},
        10: {"Numbers Only": "Instantly", "Lowercase Letters": "1 min", "Upper and Lowercase Letters": "21 hours", "Numbers, Upper and Lowercase Letters": "5 days", "Numbers, Upper and Lowercase Letters, Symbols": "2 weeks"},
        11: {"Numbers Only": "Instantly", "Lowercase Letters": "32 mins", "Upper and Lowercase Letters": "1 month", "Numbers, Upper and Lowercase Letters": "10 months", "Numbers, Upper and Lowercase Letters, Symbols": "3 years"},
        12: {"Numbers Only": "1 sec", "Lowercase Letters": "14 hours", "Upper and Lowercase Letters": "6 years", "Numbers, Upper and Lowercase Letters": "53 years", "Numbers, Upper and Lowercase Letters, Symbols": "226 years"},
        13: {"Numbers Only": "5 secs", "Lowercase Letters": "2 weeks", "Upper and Lowercase Letters": "332 years", "Numbers, Upper and Lowercase Letters": "3k years", "Numbers, Upper and Lowercase Letters, Symbols": "15k years"},
        14: {"Numbers Only": "52 secs", "Lowercase Letters": "1 year", "Upper and Lowercase Letters": "17k years", "Numbers, Upper and Lowercase Letters": "202k years", "Numbers, Upper and Lowercase Letters, Symbols": "1m years"},
        15: {"Numbers Only": "9 mins", "Lowercase Letters": "27 years", "Upper and Lowercase Letters": "898k years", "Numbers, Upper and Lowercase Letters": "12m years", "Numbers, Upper and Lowercase Letters, Symbols": "77m years"},
        16: {"Numbers Only": "1 hour", "Lowercase Letters": "713 years", "Upper and Lowercase Letters": "46m years", "Numbers, Upper and Lowercase Letters": "779m years", "Numbers, Upper and Lowercase Letters, Symbols": "5bn years"},
        17: {"Numbers Only": "14 hours", "Lowercase Letters": "18k years", "Upper and Lowercase Letters": "2bn years", "Numbers, Upper and Lowercase Letters": "48bn years", "Numbers, Upper and Lowercase Letters, Symbols": "380bn years"},
        18: {"Numbers Only": "6 days", "Lowercase Letters": "481k years", "Upper and Lowercase Letters": "126bn years", "Numbers, Upper and Lowercase Letters": "2tn years", "Numbers, Upper and Lowercase Letters, Symbols": "26tn years"}
    }

    # Get length of the password
    length = len(password)

    # Check if password length is in the lookup table
    if length in time_lookup:
        # Check if the password characteristics are in the lookup table
        for complexity, time in time_lookup[length].items():
            if password.isdigit() and "Numbers Only" in complexity:
                return time
            elif password.islower() and "Lowercase Letters" in complexity:
                return time
            elif password.isupper() and "Upper and Lowercase Letters" in complexity:
                return time
            elif password.isalnum() and "Numbers, Upper and Lowercase Letters" in complexity:
                return time
            elif not password.isalnum() and "Numbers, Upper and Lowercase Letters, Symbols" in complexity:
                return time

    return "Password is not strong enough. Consider adding more complexity."

# Example usage:
password = input("Enter your password: ")
print("Time to crack the password:", time_to_crack_password(password))

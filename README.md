# CipherHub
A tool for generating passwords and checking the complexity of passwords.

Make sure all the files are saved in the same directory.

Make sure the directories are specified properly and the correct path is specified.

If modules are missing, install them using the command below.
pip install -r requirements.txt
Make sure the modules "pyfiglet", "subprocess", "random" and "string" are installed. If not, install them manually using the command:
pip install <module_name>

Run cipher.py file

Note: Currently the password checker is only able to evaluate passwords ranging from 4 to 18 characters. A password that consist of less than 4 characters can be cracked instatntly. If a password more than 18 characters are included it shows an error message. These issues will be addressed in future updates. 

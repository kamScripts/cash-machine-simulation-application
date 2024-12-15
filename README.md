# cash-machine-simulation-application
Assignment Task. I Semester 2024/2025 FdSc Software Development

Instruction:

Dependencies:
    Pwinput -enables mask user input

Pwinput need to be installed through pip - package installer: 'pip install pwinput'.

How to Use App. 
Example credentials:
name='Tester', pin=1111, account number=111001

To log in, account number and password is required. Example accounts can be found inside App\accounts.py module. To add new account,  manually add instance of BankAccount class to the accounts list inside accounts module.
For the best experience app should be opened in command prompt by opening main.py in main folder. .After Successful login user have option to perform typical ATM operation such as withdraw, deposit, check balance. and extra option to check transfer history. Additionally, program displays number of notes equal to the withdrawal sum. User transfer history and balance are stored in separate files. In the future accounts module will be replaced with MySQL database to store user credentials.












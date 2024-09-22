# cash-machine-simulation-application
Assignment Task. I Semester 2024/2025 FdSc Software Development

Instruction:
"Your task is to create a cash machine simulation application. The application should allow users to perform simple transactions such as checking their balance, depositing money, withdrawing money, and viewing transaction history. At a basic level, the application should enable users to interact with their account through these fundamental operations. An enhanced version might include features such as multiple account types, PIN authentication, and error handling for invalid transactions."
Dependencies:
    Pwinput -enables mask user input
    re - enables matching regex patterns
Pwinput need to be installed through pip - package installer: 'pip install pwinput'.

Main objective of this project is to simulate Cash machine application. Application is constructed from two classes: Bank_Account and Cash_Machine which provide logic and mechanics for the Project. Bank_Account class provides Bank Account Management methods, such as. transfer, transaction history, and set new pin. Cash Machine simulates behavior of real ATM, which means it provides terminal for user to connect with bank and facilitate certain bank activities.

Architecture
 Project implements Oop rules. Core Sections of the project are modular, instance variables and methods are private increasing security and reducing risk of  unintended change in the future.
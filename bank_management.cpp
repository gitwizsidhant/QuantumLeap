#include <iostream>
#include <string>
#include <limits>
#include <cstdlib>
#include <ctime> // Include the ctime header for time functions
using namespace std;

class Bank
{
    string name;
    char type;
    long long int balance;
    string accountNumber; // Use a string for account number

public:
    void openAccount();
    void depositMoney();
    void withdrawMoney();
    void displaySingleAccount();
    static void displayAllAccounts(Bank accounts[], int count);
};

string generateAccountNumber()
{
    string accNum = "ACC-";
    for (int i = 0; i < 4; i++) {
        int num = rand() % 10; // Generate a random digit (0-9)
        char digit = '0' + num;
        accNum += digit;
    }
    return accNum;
}

void Bank::openAccount()
{
    cout << "Enter customer name: ";
    cin.ignore();
    getline(cin, name);
    cout << "Enter account type (s for savings, c for current): ";
    cin >> type;
    balance = 0; // Initialize balance to 0
    accountNumber = generateAccountNumber(); // Generate a unique account number
    cout << "Account created successfully. Your account number is: " << accountNumber << endl;
}

void Bank::depositMoney()
{
    string accNum;
    cout << "Enter account number: ";
    cin >> accNum;

    if (accNum == accountNumber) {
        int amount;
        cout << "Enter amount to be deposited: ";
        cin >> amount;
        balance += amount;
        cout << "Total amount deposited: " << balance << endl;
    } else {
        cout << "Account not found. Please enter a valid account number." << endl;
    }
}

void Bank::withdrawMoney()
{
    string accNum;
    cout << "Enter account number: ";
    cin >> accNum;

    if (accNum == accountNumber) {
        int amount;
        cout << "Enter amount to be withdrawn: ";
        cin >> amount;
        if (amount <= balance) {
            balance -= amount;
            cout << "Current Balance: " << balance << endl;
        } else {
            cout << "Insufficient balance." << endl;
        }
    } else {
        cout << "Account not found. Please enter a valid account number." << endl;
    }
}

void Bank::displaySingleAccount()
{
    cout << "Account Number: " << accountNumber << endl;
    cout << "Name: " << name << endl;
    cout << "Account type: " << type << endl;
    cout << "Amount Deposited: " << balance << endl;
}

void Bank::displayAllAccounts(Bank accounts[], int count)
{
    cout << "----------------------------------------------" << endl;
    cout << "Account Number | Name            | Type | Balance" << endl;
    cout << "----------------------------------------------" << endl;
    for (int i = 0; i < count; i++) {
        cout << accounts[i].accountNumber << "             | ";
        cout << accounts[i].name << " | ";
        cout << accounts[i].type << "    | ";
        cout << accounts[i].balance << endl;
    }
    cout << "----------------------------------------------" << endl;
}


int main()
{
    int choice;
    const int maxAccounts = 100; // Maximum number of accounts
    Bank accounts[maxAccounts];
    int accountCount = 0;

    // Seed the random number generator
    srand(time(0));

    cout << "Welcome to the Bank Management System" << endl;

    do
    {
        cout << "\n1. Open account" << endl;
        cout << "2. Deposit money" << endl;
        cout << "3. Withdraw money" << endl;
        cout << "4. Display single account" << endl;
        cout << "5. Display all accounts" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            if (accountCount < maxAccounts) {
                accounts[accountCount++].openAccount();
            } else {
                cout << "Maximum number of accounts reached." << endl;
            }
            break;

        case 2:
            if (accountCount > 0) {
                accounts[0].depositMoney();
            } else {
                cout << "No accounts available." << endl;
            }
            break;

        case 3:
            if (accountCount > 0) {
                accounts[0].withdrawMoney();
            } else {
                cout << "No accounts available." << endl;
            }
            break;

        case 4:
            if (accountCount > 0) {
                accounts[0].displaySingleAccount();
            } else {
                cout << "No accounts available." << endl;
            }
            break;

        case 5:
            if (accountCount > 0) {
                Bank::displayAllAccounts(accounts, accountCount);
            } else {
                cout << "No accounts available." << endl;
            }
            break;

        case 6:
            cout << "Exiting program" << endl;
            break;

        default:
            cout << "Wrong entry, try again" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    } while (choice != 6);

    return 0;
}

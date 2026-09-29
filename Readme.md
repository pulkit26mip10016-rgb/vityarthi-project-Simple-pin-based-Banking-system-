Simple PIN-Based Banking System (Console Application)

📌 Project Title
Simple PIN-Based Banking System**

 📖 Overview
This is a simple ATM/banking system made in Python. When you run it, you get two choices either log in with an existing PIN** or create a new account.

If you enter a correct pin (must be 4 digits, and only made up of the digits 6, 7, 8, 9), you're logged in and taken to a menu where you can check your balance, deposit money, withdraw money, or exit. If you choose to create a new account instead, you enter your name and keep entering pins until you pick one that isn't already taken, then set your starting deposit.

All customer data (name, pin, balance) is kept in lists while the program runs  it doesn't save anything permanently, so it resets every time you restart the program.

 ✨ Features
- PIN Login checks a 4-digit pin (only digits 6,7,8,9 allowed) against existing customer records.
- Account Creation lets a new user pick a name and a unique pin (keeps asking until you enter one that's not already taken), then sets an initial deposit.
- Balance Enquiry  shows your current balance.
- Deposit  adds an entered amount to your balance.
- Withdraw takes money out, but blocks it if the amount is more than your balance or negative.
- Exit  ends the session with a thank-you message.
- Invalid Menu Choice Handling  inside the account menu, if you type something other than 1-4, it tells you it's invalid instead of doing nothing.

 🛠️ Technologies / Tools Used
- **Language:** Python 3
- **Concepts Used:** lists, loops (while,for), conditional statements, input handling, basic validation
- **Environment:** Any system with Python 3 installed  no extra libraries needed

 📂 Project Structure
```
banking-system/

 code3.py        # main script - login, account creation, deposit/withdraw logic
 README.md       # this file


 ⚙️ Steps to Install & Run

1. Install Python 3** if it's not already on your system
   - Download from [python.org](https://www.python.org/downloads/)
   - Check it's installed:
     ```bash
     python --version
     ```

2. Get the project files**
   ```bash
   git clone <your-repository-link>
   cd banking-system
   ```

3. Run the program
   ```bash
   python code3.py
   ```

4. Follow the prompts on screen enter 1 to log in or 2 to create a new account, then follow further prompts.

 🧪 Instructions for Testing

Test 1  Login with an existing pin
1. Run the program, enter 1.
2. Enter a pin from the pre-loaded list, e.g. 6789.
3. Check that the welcome message shows the right customer name.
4. Pick 1 to check balance and confirm it matches the starting value.

Test 2  Deposit
1. Log in with a valid pin.
2. Pick 2, enter an amount (e.g. 500).
3. Confirm the balance goes up correctly.

Test 3  Withdraw
1. Log in with a valid pin.
2. Pick 3, enter an amount less than your balance.
3. Confirm the balance goes down and the "Here is your money" message shows.
4. Try withdrawing more than your balance and confirm it says "Insuficient amount".
Test 4  Wrong pin
1. At login, enter a pin that's not 4 digits or uses digits other than 6-9.
2. Confirm it prints "invalid pin".
3. Enter a correctly-formatted pin that doesn't exist in the list.
4. Confirm it prints "pin Doesn't exist".

Test 5  Create a new account
1. Run the program, enter 2.
2. Enter your name, then a new 4-digit pin (digits 6-9 only) that isn't already used.
3. Enter a starting deposit amount.
4. Confirm the account gets created and the balance shows correctly.
5. Try entering a pin that already exists  confirm it says "pin already exist" and asks again.

Known limitation to flag while testing: entering a non-numeric value where a number is expected (like the deposit amount, withdrawal amount, or menu choice) will crash the program, since there's no error handling around int(input(...)) calls yet.

 📸 Screenshots
(Add terminal screenshots here showing login, deposit, and withdrawal once available.)

 🚀 Future Enhancements
- Save data to a file or database so accounts persist between runs.
- Add proper error handling so the program doesn't crash on bad input.
- Break the code into functions (login, deposit, withdraw, etc.) for better modularity.
- Hide the pin while typing instead of showing it on screen.
- Add transaction history.


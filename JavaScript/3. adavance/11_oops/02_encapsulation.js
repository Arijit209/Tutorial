class bankAccount {
    #balance = 0; // private property   
    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    // Public method to deposit money
    deposit(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance += amount;
            console.log(`Deposited: $${amount}. New Balance: $${this.#balance}`);
        } else {
            console.log('Deposit amount must be positive.');
        }
    }

    // Public method to withdraw money
    withdraw(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance -= amount;
            console.log(`Withdrew: $${amount}. New Balance: $${this.#balance}`);
        } else {
            console.log('Invalid withdrawal amount.');
        }
    }

    getBalance() {
        return this.#balance;
    }
}
const myAccount = new bankAccount(1000);
myAccount.deposit(500); // Output: Deposited: $500. New Balance: $1500
myAccount.withdraw(200);
console.log(`Current Balance: $${myAccount.getBalance()}`); // Output: Current Balance: $1300
myAccount.withdraw(1500); // Output: Invalid withdrawal amount.
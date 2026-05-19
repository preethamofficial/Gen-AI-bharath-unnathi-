import java.util.Scanner;

class BankAccount {
    String name;
    String accNo;
    double balance;

    // Constructor
    BankAccount(String name, String accNo, double balance) {
        this.name = name;
        this.accNo = accNo;
        this.balance = balance;
    }

    // Deposit method
    void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid amount!");
            return;
        }
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    // Withdraw method
    void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid amount!");
        } else if (amount > balance) {
            System.out.println("Insufficient Balance!");
        } else {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        }
    }

    // Check balance
    void checkBalance() {
        System.out.println("Current Balance: " + balance);
    }

    // Display account details
    void displayDetails() {
        System.out.println("\n--- Account Details ---");
        System.out.println("Name: " + name);
        System.out.println("Account Number: " + accNo);
        System.out.println("Balance: " + balance);
    }
}

public class BankSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Smart Bank Management System ===");

        System.out.print("Enter Account Holder Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Account Number: ");
        String accNo = sc.nextLine();

        System.out.print("Enter Initial Balance: ");
        double balance = sc.nextDouble();

        BankAccount account = new BankAccount(name, accNo, balance);

        while (true) {
            System.out.println("\n===== MENU =====");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Account Details");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");

            if (!sc.hasNextInt()) {
                System.out.println("Invalid input! Enter a number.");
                sc.next(); // clear invalid input
                continue;
            }

            int choice = sc.nextInt();

            if (choice == 1) {
                System.out.print("Enter amount to deposit: ");
                double amount = sc.nextDouble();
                account.deposit(amount);

            } else if (choice == 2) {
                System.out.print("Enter amount to withdraw: ");
                double amount = sc.nextDouble();
                account.withdraw(amount);

            } else if (choice == 3) {
                account.checkBalance();

            } else if (choice == 4) {
                account.displayDetails();

            } else if (choice == 5) {
                System.out.println("Thank you for using the system!");
                break;

            } else {
                System.out.println("Invalid choice! Try again.");
            }
        }

        sc.close();
    }
}
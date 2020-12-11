Data storage is pretty boring if it's just read-only- we want to write and delete stuff as well. One of the most important responsibilities of a good database or storage system is maintaining consistent and accurate data no matter what happens. 

A **transaction** is like a package that contains changes to be made to a database/storage. Transactions follow the ACID property:

- **Atomic**: All actions completed or nothing is
- **Consistent**: Changes data in allowed ways + future transactions will see past transactions
- **Isolated**: Independent of other transactions
- **Durable**: Updates are made to *persistent* storage.

Following the ACID properties are intended to ensure that data stays valid even in the cases of power failure, errors, or accidental corruption/miscommunication by peers. Specifically, ACID also provides isolation between *concurrent* database accesses.

A very common example of transactions (Xacts for short) are bank account transfers. A transfer Xact consists of both subtraction from the transferrer account and addition to the receiver account. 


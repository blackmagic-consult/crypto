## Notes about the Product Code Algorithim

There are two userflows - those that purchase a friends card via the app (simple), and those that buy a physical friends card and want to use that application.

For the second usergroup, we need to generate a Verifiable, non-repeating product code that can be printed on the physical friends card, easy to type in, and independently verifiable without (preferably) maintaining an independent database of useable codes.

The traditional method of generating a product code is taking the users email, adding a salt, and hashing it into a independently verifiable code. This is secure enough for most purposes and is unlikely to generate the same code twice, since most people don't have the same email.

However, we need a way to generate the codes with the same amount of randomness WITHOUT requiring user input, since the cards will be printed beforehand. This is actually fairly tricky without maintaining a database of valid codes, which we don't want to do because it would be reasonably expensive to securely maintain.

The following code snippet demonstrates a quasi-functional solution.

[https://gist.github.com/blackmagic-consult/f3d2980dda8ec8c73141b06ada4d91dd](https://gist.github.com/blackmagic-consult/f3d2980dda8ec8c73141b06ada4d91dd)

Problems arise; The hash generation is simply not random enough.

Solutions:

1. Use the exact Atomic time & date of the exact moment the code is generated for the random hash (Just extends the problem for someone else to solve)
2. Use a longer hash. Decreases readability.
3. Keep a database of valid codes. Expensive, hard to maintain.

### Related Reading

[How to generate and validate a software license key?](https://stackoverflow.com/questions/599837/how-to-generate-and-validate-a-software-license-key)

[Generating License Keys in 2019](https://build-system.fman.io/generating-license-keys)

[How are software license keys generated?](https://stackoverflow.com/questions/3002067/how-are-software-license-keys-generated)

[How do I create a software serial key?](https://www.quora.com/How-do-I-create-a-software-serial-key)

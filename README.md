# inet_4031_adduser_script
Automating user creation on Ubuntu.

#Description
This Python script automates the creation of user accounts on an Ubuntu system. It reads user information from an input file and performs the following tasks for each user:
- Creates a new user account.
- Sets the user's password.
- Assigns the user to specified groups.

#Program Operation
1. **Reading Input:**
   - The script reads each line from `create-users.input` using `sys.stdin`
   - It checks if a line is a comment (starts with `#`) or if the line does not contain exactly 5 fields and skips such lines.

2. **Creating User Accounts:**
   - For valid lines, the script uses the `adduser` command to create a user account with a disabled password and sets user details like `gecos`.

3. **Setting Passwords:**
   - The script uses the `passwd` command to set the password for each user, using `sudo` to ensure the operation has the necessary permissions.

4. **Assigning Groups:**
   - The script checks the groups specified for each user and adds the user to the appropriate groups, unless the group field contains `-`, which means no group assignment.

5. **Output Messages:**
   - The script prints messages to the console indicating the status of each operation, such as creating an account, setting a password, and assigning groups.


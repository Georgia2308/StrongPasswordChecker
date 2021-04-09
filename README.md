Strong Password Checker Application

Summary
The password checker is a console application built in Python whose purpose is to generate a strong password according to the following conditions:
1.	It has at least 6 characters and at most 20 characters.
2.	It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
3.	It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
The user can input any password and will receive a recommended alternative with the minimum number of changes, where one change is considered to be either the insertion, replacement or deletion of a character. An entirely new strong password can also be generated if the user offers no input. Runtime ends when the user presses ‘.’ . If the given password is already strong, the output is instead ‘0’.
In building the application, I assumed the following:
•	Special characters (ex. / , . etc) are allowed.
•	Spaces, however, are not allowed.
•	Uppercase and lowercase variants of the same letter are considered different characters.
Algorithm description
The algorithm is designed to receive a password as a string and proceeds to construct variables that keep track of all the relevant character positions (such as lowercase, uppercase, digits, symbols) as well as problematic repeating characters. It also maintains a count of the changes made, if any.
Once the input is validated, the algorithm checks all required conditions, starting with the length of the password. If there are over 20 characters, the adjacent repeating characters are eliminated first (if they exist), otherwise any character can be removed unless it conflicts with the conditions (the last lowercase/uppercase/digit will not be removed).
Next up, the algorithm checks the existence of at least one lowercase, one uppercase and one digit. If these are insufficient, it finds the optimal position to insert one, as such:
1.	If length is insufficient, it adds a new character.
2.	If there are repeating characters, it replaces them.
3.	If there are any symbols, it replaces those.
4.	If there are available uppercase/lowercase/digit positions, replace them.
5.	Otherwise, adds a new character.
If at this point there still are too many repeating characters, those are also replaced.
Finally, if the character count is too small (<6) new characters are added.
All of these operations are performed while checking adjacent positions, ensuring no new problems are created by having repeating characters. A function is used to find the recommended character to insert on a certain position while respecting the conditions.
Once this process is finished, the modified password is displayed along with the number of changes performed. 

# password-Generator-project.
This repository contain my password generator project
Password Generator
Python Project — README
v1.0  |  Python 3.8+  |  Beginner Level


Project Overview
Yeh project ek command-line password generator hai jo user ke options ke hisaab se strong, random passwords generate karta hai. Yeh project Python ke basics — string manipulation, random module, aur user input — seekhne ke liye perfect hai.

Features
Feature	Description
Custom Length	6 se 32 characters tak password length set karo
Capital Letters	Uppercase A-Z include/exclude karo
Numbers	0-9 digits include/exclude karo
Symbols	!@#$%^&* jaise special characters add karo
Multiple Passwords	Ek baar mein multiple passwords generate karo
Strength Meter	Password ki strength automatically check hoti hai



Requirements
Python Version
Python 3.8 ya usse upar zaroori hai.

Dependencies
Koi bhi external library install nahi karni — sirf Python standard library use hoti hai:

•random — random characters pick karne ke liye
•string — pre-built character sets (lowercase, uppercase, digits, punctuation)
•secrets — zyada secure passwords ke liye (optional upgrade)



Installation aur Setup
Step 1: Python Install Karo
Pehle check karo Python installed hai ya nahi:

python --version

Agar nahi hai toh python.org se download karo.

Step 2: Project Files
Yeh files apne project folder mein rakhni hain:

password_generator/
    password_generator.py    # main file
    README.md                # yeh file

Step 3: Run Karo
Terminal/command prompt mein yeh command chalao:

python password_generator.py



Usage
Program Chalane ka Tarika
Program chalane ke baad yeh prompts aayenge — inka jawab do:

1.Password ki length kitni ho? (default 12)
2.Capital letters include karo? (y/n, default y)
3.Numbers include karo? (y/n, default y)
4.Symbols (!@#$) include karo? (y/n, default y)
5.Kitne passwords generate karo? (default 1)

Sample Output
=== Password Generator ===

Password ki length kitni ho? (default 12): 16
Capital letters include karo? (y/n): y
Numbers include karo? (y/n): y
Symbols include karo? (y/n): y
Kitne passwords generate karo? (default 1): 3

--- Tumhare 3 Password(s) ---
1. kR#9mLx@2pQvT!n  [Bohot Strong]
2. Wz$4bN&8qY*1cXs  [Bohot Strong]
3. jM@7eP#5rK!2uHt  [Bohot Strong]



Code Structure
Functions
Function	Kaam
generate_password()	Options ke hisaab se random password banata hai
get_strength()	Password ka strength score calculate karta hai
main()	User se input leta hai aur sab functions call karta hai

Strength Scoring System
Password ki strength yeh criteria se measure hoti hai:

•Length >= 8:  +1 point
•Length >= 12: +1 point
•Length >= 16: +1 point
•Uppercase include: +1 point
•Numbers include: +1 point
•Symbols include: +2 points

Score	Label	Matlab
0-2	Kamzor	Asaani se guess ho sakta hai
3-4	Theek Hai	Basic security ke liye kaafi
5	Acha	Zyada tar cases mein safe
6-7	Bohot Strong	High security ke liye best



Future Improvements (Next Steps)
Is project ko aur behtar banane ke liye yeh features add kar sakte ho:

•GUI version — tkinter se window-based app banao
•Clipboard copy — pyperclip se automatically copy ho
•Password history — generated passwords ko file mein save karo
•Custom symbols — user apne symbols define kare
•Exclude ambiguous — O, 0, l, 1 jaise confusing characters hatao
•secrets module — cryptographically secure generation ke liye upgrade

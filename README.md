
          TASK 2: PLAIN-ENGLISH TEST AUTOMATION (PYTHON + PLAYWRIGHT + GEMINI)


1. WHAT IT IS & HOW IT WORKS (IN SIMPLE WORDS)
--------------------------------------------------------------------------------
You write what to test in normal plain English (no code, no XPath, no selectors):
> "Go to https://the-internet.herokuapp.com/login, log in with username tomsmith 
   and password SuperSecretPassword! and verify the secure area message is shown"

The tool repeats a simple 3-step loop:
1. LOOK   -> Reads the webpage and makes a numbered list of all clickable buttons 
             and input boxes.
2. THINK  -> Sends your sentence and that numbered list to Gemini and asks: 
             "What should I do next?"
3. DO     -> Playwright performs that action (typing, clicking) in real Chromium.
4. REPEAT -> Keeps going until the goal is finished.
5. CHECK  -> The "Honesty Check": To count as a PASS, the AI must quote exact proof 
             text directly from the page. If the text is not really on 
             the screen, the pass is rejected!


2. HOW TO SET UP & RUN (COMMANDS)
--------------------------------------------------------------------------------
Open PowerShell inside your task2 folder:
cd C:\Users\Ragini\Downloads\task2-english-to-test_claudeMade\task2-english-to-test

Step 1: Activate the virtual environment:
.\venv\Scripts\Activate.ps1

(Note: If PowerShell blocks scripts, run this once:
 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)

Step 2: Check your API key and active Gemini models:
python nl_test.py --list-models

Step 3: Run Test Case 1 (The Internet Herokuapp Login):
python nl_test.py "Go to https://the-internet.herokuapp.com/login, log in with username tomsmith and password SuperSecretPassword! and verify the secure area message is shown"

Step 4: Run Test Case 2 (SauceDemo Login):
python nl_test.py "Go to https://www.saucedemo.com, log in with username standard_user and password secret_sauce, and verify Products is shown"

Step 5: Run both tests together from a file:
python nl_test.py --file tests.txt

Step 6: Run for Video Demo Recording (slows down actions + stays open):
python nl_test.py --file tests.txt --slow-mo 300 --keep-open

Step 7: Check test reports and step screenshots:
explorer runs


3. LIMITATIONS (IN SHORT & SIMPLE WORDS)
--------------------------------------------------------------------------------
1. Slower than Hardcoded Scripts: 
   - Because it consults an AI model at each step, a test takes 15 to 45 seconds instead of 2 seconds.

2. Needs Active AI API & Quota: 
   - If the AI service is busy or daily free limits run out, tests must wait or retry.

3. Cannot Solve Bot Shields & CAPTCHAs: 
   - It cannot bypass Cloudflare turnstiles or image puzzles (like on PHPTravels).

4. Verifies Text, Not Visual Styling: 
   - It checks that the expected confirmation words exist in the page text. It does not check visual layout, fonts, or colors.

5. Main Page Only: 
   - It currently does not inspect elements hidden inside cross-domain iframes or closed Shadow DOM trees.
================================================================================

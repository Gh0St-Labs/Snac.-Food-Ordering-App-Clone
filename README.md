# Snac. (ip)

An institutional food ordering app for in-done celebrations.

--------------------------------_

- Usage and Working Comprehension
__ Snac. uses Streamlit as it's web-structure and carries out tasks similar to food ordering apps, for instance, UberEats.

__ Snac. is built for institutional purposes and involves ordering snacks, circumnavigating around the school's celebrations such as Fests, A-Days and F-Days.

__ Once opened, you'll be greeted with a list of celebrations that are in effect. 

__ The correct celebration should be chosen, which will have it's own menu.

__ Once you're snacks have been selected from this menu, you'll then view a popup right below to select the quantity of each item. 

__ Now, when the preferred quantities are selected for their snacks, you can then confirm you're order by a payment. 

__ If the payment is successful, you will then be re-directed to a QR Code generation, where you will be generated a QR Code for the provider to scan it.

__ The QR Code consists of you're order of snacks, with the right quantity that you've selected.

__ The provider scans the QR Code and notes your order, eventually fulfilling it by providing the snacks to you.

--------------------------------_

- Files

__ The "Snac.py" file consists of code which is the main workflow of the project.

__ "Instructions.py" does not contain the instructions for the app and project setup. Rather, it contains the instructions for using "Snac.", which will be added once further insights 
are recieved.

--------------------------------_

- Setup 

__ Make a directory (folder) in your workspace. 

__ Add in both "Snac.py" and "Instructions.py" into the folder.

__ Create a sub-folder named "pages" inside this folder, which now contains both the files.

__ Move the "Instructions.py" into the "pages" sub-folder.

__ Use VS Code and add in your main folder, created formerly, into your environment.

__ Now, your environment inside VS Code contains the main folder, where you can access it's sub-file, which is "Snac", and it's sub-folder, "pages", with it's sub-file, "Instructions".

__ In your environment, open "Snac.py".

__ Right-click on your main folder that shows on the right. Then, click on "Open in integrated terminal" to open it's own terminal.

__ Once your terminal is opened, run these commands to first download some requirements:

    _ _ _ _ _ } pip install streamlit

    _ _ _ _ _ } pip install --upgrade streamlit

    _ _ _ _ _ } pip install qrcode.

__ Do not do this simultaneously; run each command seperately and wait for it to completely finish.

__ Next, once you've downloaded the requirements, you can run the app using:

    _ _ _ _ _ } streamlit run Snac.py

__ This will open the app in a "localhost" with it's own ID generated by streamlit itself.

- Further Changes

__ The further changes that has to be put in are:

    > Payment Gateaway
    > Domain Name
    > Database
    > CSS Styling and "Eye-pleasers"
    > Continous Domain Hosting

__ Once these are crowned, Snac. is up for deployment. 
 

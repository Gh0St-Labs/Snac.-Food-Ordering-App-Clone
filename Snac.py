import streamlit as st
import qrcode as qr
from io import BytesIO
from base64 import b64encode

# Setting page configuration
st.set_page_config(
    page_title="Snac. | #wop",
    page_icon="🍴",
    layout='centered',
    initial_sidebar_state='expanded'
)

# ---------------------------- Welcome Page

# Names and Authenticity
st.title("Snac.")

# ..
st.markdown("---")

# Motto
st.caption('Tastebuds, triumphed.')

# Fest Choosing
st.subheader("Choose the preferred fest that you recide in:")
fest = st.selectbox("Fests available:", ("TIPS Basketball Meet 2022", "TIPS Soccer Meet 2023", "TIPS Badminton Meet 2024"))

# >>>> Pages
# Pages involved (excluding Main Page)
# 1. Menu Page
# 2. Checkout Page with QR generation

# NOTE: Pages are chosen from the sidebar and uses different python files that act as pages. To see them, go to 
# "pages".

st.sidebar.success("Note: Foods should be selected after choosing the fest.")


# ---------------------------- For Menu, Orders and generating QR

fests = {"TIPS Basketball Meet 2022":"1", "TIPS Soccer Meet 2023":"2", "TIPS Badminton Meet 2024":"3"}
menus = {"1":['Nachos', 'Nachos with Dip', 'Brownie with Icecream', 'Lemonade', 'Samosas'], 
         "2":['Mushroom Pizza Slice', 'Nachos with Dip', 'Veg Nuggets'], 
         "3":['Masala Corn', "Buttered Corn", "Nachos with Dip", "Lemonade", "Coffee - Large", "Coffee - Medium"]}

# List for use
addedOrders = []

# ////// IMPORTANT TBD: Make a mechanism in which customers can select the available foods from a dropdown box 
# ONCE, unlike the multiselect, and then add in the quantity of that selected food from an input box next to it.

# Getting the menu and the menu items from the selected fest in "Welcome.py"
for aFest in fests:
    if aFest == fest:
        menu = fests[aFest]
        menuItems = menus[menu]

        # List for use
        menuItemsToSelect = []

        for menu in menuItems:
            menuItemsToSelect.append(menu)

        # Display the menu items in the selectbox
        order = st.multiselect('Choose your foods:', menuItemsToSelect)

# Select Quantity Label
st.markdown("<center><i> First, Select your snacks and Select the quantity below. </i></center>", 
            unsafe_allow_html=True)

# Multiple item selection from the list of the "order" variable.

quanList = []

def quantifyOrder(ordervar):

    for anOrder in ordervar:
        quantities = st.slider(anOrder, min_value=1, max_value=5)

        for quantity in str(quantities):
            quanList.append(quantity)

# Quantify order
quantifyOrder(order)

# Finalize order
orderFinal = f"{[item for item in order], [snackQuantity for snackQuantity in quanList]}"

# Line
st.markdown("---")

# Button to verify the order
emptycol1, emptycol2, orderDoneCol, retakeOrderCol, emptycol3, emptycol4 = st.columns(6)

with orderDoneCol:
    doneButton = st.button('Done With My Order')

with retakeOrderCol:
    retakeOrderButton = st.button('Retake My Order')

if doneButton and len(order) != 0:

    # Generating QR Code based on the order of the customer; using "order" variable.

    memory = BytesIO()
    # Creating a memory-space so that the image can be stored, in bytes.

    img = qr.make(orderFinal)
    # Make the QR Code

    img.save(memory)
    # Save the QR Code to the memory in bytes.

    # Convert the saved, byte-stored QR Code image into a "base64" using the 'b64encode' function to get the image 
    # all in one place.
    b64Img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')

    # So, now, 'b64Img' is the image variable to be displayed.

    # Logic of centering the image with the page.
    anoEmptyCol, imgCol, anoEmptyCol2 = st.columns(3)
    with imgCol:
        
        #Blanks
        st.write("")
        st.write("")

        # The image.
        st.image(b64Img, caption='Your QR Code for the order. Show this to our students serving and enjoy snacking.')


else:
    None
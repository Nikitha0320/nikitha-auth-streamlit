import streamlit as st
#header
st.divider()
st.header("GUJJURI NIKITHA")
st.divider()
st.header("Header")

#title
st.divider()
st.title("Title")

#subheader
st.divider()
st.subheader("Subheader")

#markdown horizontal line
st.divider()
st.markdown("---------------")

#text method to display information
st.divider()
st.text("This is text method")

#write text,number,list,dictionary 
st.divider()
st.write("This is write method")
st.write(12345)
st.write(["Streamlit", "is", "awesome"])

#markdowm method to display formatted text
st.divider()
st.markdown("### this is markdown ###")
st.markdown("**bold text**")
st.markdown("*italic text*")
st.markdown("- item 1\n- item 2")
st.markdown("<h3 style='color:red'>Red Text</h3>", unsafe_allow_html=True)

#caption method to add captions
st.divider()
st.caption("This is caption method")

#code method to diaplay code snippets
st.divider()
st.code("""
        def add(a,b):
            return a+b
        """, language='python')

#latex method to render mathematical expressions
st.divider()
st.latex(r'''
a^2 + b^2 = c^2
''')

#divider method to add horizontal dividers
st.divider()

#button method to create clickable buttons
if st.button("Click Me"):
    st.success("Button Clicked!")
    st.snow()
else:
    st.write("click the button")
    st.error("Button not clicked yet.")

#text input method to get user input
st.divider()
name = st.text_input("Enter your name:")
if name=='':
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("Please enter a valid name.")
else:
    st.success(f"Hello, {name}!")

#multiline text input method
st.divider()
message = st.text_area("Enter your message:")
st.write("Your message:", message)

#checkbox method to create checkboxes
st.divider()
if st.checkbox("I agree to the terms and conditions"):
    st.success("Thank you for agreeing!")
else:
    st.write("Please agree to continue.")

#radio button method to create radio buttons
st.divider()
gender = st.radio("Select your gender:", ("Female","Male", "Other"))
st.write("You selected:", gender)

#selectbox method to create dropdown menus
st.divider()
country = st.selectbox("Select your country:", ["India","USA", "Canada", "UK", "Australia"])
st.write("Country:", country)

#multiselect method to allow multiple selections
st.divider()
fruits = st.multiselect("Select your favorite fruits:", ["Apple","Banana", "Mango", "Orange", "Grapes"])
st.write("Fruits:", fruits)

#slider method to create sliders
st.divider()
age = st.slider("Select your age:", 0, 100, 25)
st.write("Age:", age)

#file uploader method to upload files
st.divider()
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
else:
    st.info("Please upload a file.")

#form method to create forms
st.divider()
with st.form("my_form"):
    st.write("Fill out the form:")
    name = st.text_input("Name:")
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Form submitted! Name: {name}")

#form_submit_button method to submit forms
st.divider()
with st.form("another_form"):
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    submit_button = st.form_submit_button("Login")
    if submit_button:
        st.success("Login successful!")

#column method to create columns
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1")
with col2:
    st.header("Column 2")
    st.write("This is column 2")
with col3:
    st.header("Column 3")
    st.write("This is column 3")

#container method to create containers
st.divider()
with st.container():
    st.header("Container")
    st.write("This is inside a container")
    with st.form("container_form"):
        feedback = st.text_area("Your feedback:")
        submit_feedback = st.form_submit_button("Submit Feedback")
        if submit_feedback:
            st.success("Feedback submitted!")

#table method to display data in tabular format
st.divider()
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

#sidebar method to create a sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

#cache method to cache function outputs
st.divider()
st.write("Cached Data Example:")
@st.cache_data
def load_data():
    return [1,2,3,4,5]
data = load_data()
st.write(data)

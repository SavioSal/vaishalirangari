
import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", layout='wide')

st.header("Vaishali Rangari - Business Analyst")
st.write("\n\n")
col1, col2 = st.columns([1,2])
col1.image("business analyst badge.png", use_column_width=True)
col2.write("This site serves as a testament to the business analysis skills exhibited by Vaishali Rangari. \
          \n\nShe possesses business analyst work experience. This site was built by Vaishali as a business analyst and the educator team at \
          \n\nSavio Education Global as part of her business analyst work experience. \
          \n\nHer work included creating the BRD, FRD, User Stories, Data Model, Wireframe, Data Visualization using Tableau, Test Scenarios, Test Cases, Defect Reports and working with Atlassian JIRA.\
          \n\nCongratulations Vaishali! You did well and we're proud of your work!")
col2.write("This site is created based on wireframes created by Vaishali.")
c1, c2 = st.columns([4,1])

with c1:
    products = st.selectbox(label = "Search products", placeholder="Search Products", 
                label_visibility="hidden", index=None,
                options=["Business Analyst", "Machine Learning Engineer"])

    st.subheader("Featured Products", anchor=False)

    col1, col2 = st.columns(2,gap="large")

    col1.image("business analyst 8 weeks.jpg")
    col1.link_button("Know more", "/business-analyst-work-experience-program")

    col2.image("ml engineer compressed.jpg")
    col2.link_button("Know more", "/machine-learning-engineer-work-experience-program")
    
with c2:
    st.write("")
    st.write("")
    st.link_button("Login", "/Login", type="primary")
    st.button("Signup")

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
col1, col2, col3 = st.columns(3)
col1.button("About Us")
col2.button("Contact Us")
col3.button("Reviews")
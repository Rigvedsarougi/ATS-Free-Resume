import streamlit as st
import subprocess

def generate_resume(name, location, phone, website, email, linkedin, github):
    with open("main.tex", "r") as file:
        template = file.read()
    
    # Replace placeholders with user inputs
    template = template.replace("{\large John Smith}", "{\large " + name + "}")
    template = template.replace("{Salt Lake City, Utah}", location)
    template = template.replace("{111-111-1111}", phone)
    template = template.replace("{https://website}", website)
    template = template.replace("{email@email.com}", email)
    template = template.replace("{https://linkedin.com/in/username}", linkedin)
    template = template.replace("{https://github.com/sansquoi}", github)
    
    # Write the modified template to a new file
    with open("generated_resume.tex", "w") as file:
        file.write(template)
    
    # Compile the LaTeX file to generate PDF
    subprocess.run(["pdflatex", "generated_resume.tex"])

# Streamlit UI
st.title("Resume Generator")

name = st.text_input("Full Name")
location = st.text_input("Location")
phone = st.text_input("Phone")
website = st.text_input("Website")
email = st.text_input("Email")
linkedin = st.text_input("LinkedIn")
github = st.text_input("GitHub")

if st.button("Generate Resume"):
    generate_resume(name, location, phone, website, email, linkedin, github)
    st.success("Resume generated successfully!")

    # Provide download link for the generated PDF
    st.markdown("[Download PDF](generated_resume.pdf)", unsafe_allow_html=True)

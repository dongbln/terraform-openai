# Import necessary modules 
import streamlit as st 
import openai

# Set the title of the Streamlit application
st.title("DevOps Engineer meet AI Demo")

# Request user to input OpenAPI API Key
api_key = st.sidebar.text_input("Enter OpenAPI API Key", type="password")

def chatGPT(prompt):   
    completion = openai.Completion.create(
                                  engine = "text-davinci-003",
                                  prompt = prompt,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.0,
                                      )
    response = completion.choices[0].text
    return response


# Check if the user has entered an API key
if api_key:
  

    openai.api_key = api_key
    
    # Request the user to enter a question
    prompt = st.text_area("Enter a command to create a Terraform code ", "write a complete Terraform code  to provision azure storage account gen2 with the account name: mydevopsaccount, resource group name: rg-devops-001, the location is West Europe, and add identity ")    
    
    # Check if the "Generate Answer" button is pressed
    if st.button("Generate Terraform"):
        # Check if the user has entered a question
        if prompt:
            # While the answer is being generated, show a loading spinner
            with st.spinner("Generating Terraform..."):
              
                answer = chatGPT(prompt=prompt)
                # Display the generated answer
                st.code(answer,language="Terraform")
        else:
            # Display a warning if the user hasn't entered a question
            st.warning("Please enter a command")
else:
    # Display a warning if the user hasn't entered an API key
    st.warning("Please enter OpenAPI API Key!")

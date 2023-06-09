import streamlit as st
from streamlit_chat import message
import os

# Using OPENAI LLM's
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory

st.set_page_config(
    page_title="Assistant",
    page_icon=":robot:"
)

# state to hold generated output of llm
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# state to hold past user messages
if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'textbox' not in st.session_state:
    st.session_state['textbox'] = ""

if 'infotext' not in st.session_state:
    st.session_state['infotext'] = ""

def initModel(template):
    llm = OpenAI(temperature=10e-3)
    memory = ConversationBufferMemory(memory_key="history")
    prompt = PromptTemplate(input_variables=["input", "history"], template=template)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory
    )
    st.session_state.conversation = llm_chain

with st.sidebar:
    st.header("Welcome to Assistant")
    st.markdown("A ChatBot powered by OpenAI GPT")
    os.environ["OPENAI_API_KEY"] = st.text_input("[OPENAI_API_KEY](https://platform.openai.com/account/api-keys)", "")
    state = st.selectbox("Select Template", ["career-counselour", "financial-analyst","recruiter","UI/UX","math-teacher", "advertiser", "prompt-generator","password-generator", "english-translator", "travel-guide"])
    if st.button("Confirm"):
        st.session_state.past = []
        st.session_state.generated = []
        st.session_state.textbox = ""
        match state:
            case "financial-analyst":
                template = """Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely!
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Assisting you with financial decisions."
                initModel(template)
            case "career-counselour":
                template = """I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "I am Recruiter! Helping you with sourcing strategies."
                initModel(template)
            case "recruiter":
                template = """I want you to act as a recruiter. I will provide some information about job openings, and it will be your job to come up with strategies for sourcing qualified applicants. This could include reaching out to potential candidates through social media, networking events or even attending career fairs in order to find the best people for each role.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "I am Recruiter! Helping you with sourcing strategies."
                initModel(template)
            case "UI/UX":
                template = """I want you to act as a UX/UI developer. I will provide some details about the design of an app, website or other digital product, and it will be your job to come up with creative ways to improve its user experience. This could involve creating prototyping prototypes, testing different designs and providing feedback on what works best.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Assisting you in UI/UX!"
                initModel(template)
            case "math-teacher":
                template = """I want you to act as a math teacher. I will provide some mathematical equations or concepts, and it will be your job to explain them in easy-to-understand terms. This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "I can teach you Math! Ask me anything."
                initModel(template)
            case "advertiser":
                template = """I want you to act as an advertiser. You will create a campaign to promote a product or service of your choice. You will choose a target audience, develop key messages and slogans, select the media channels for promotion, and decide on any additional activities needed to reach your goals.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Welcome to Advertiser! Input topic to start your campaign!"
                initModel(template)
            case "prompt-generator":
                template = """I want you to act as a ChatGPT prompt generator, I will send a topic, you have to generate a ChatGPT prompt based on the content of the topic, the prompt should start with "I want you to act as ", and guess what I might do, and expand the prompt accordingly Describe the content to make it useful.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Welcome to prompt generator! Create prompts based on topics."
                initModel(template)
            case "password-generator":
                template = """I want you to act as a password generator for individuals in need of a secure password. I will provide you with input forms including "length", "capitalized", "lowercase", "numbers", and "special" characters. Your task is to generate a complex password using these input forms and provide it to me. Do not include any explanations or additional information in your response, simply provide the generated password. For example, if the input forms are length = 8, capitalized = 1, lowercase = 5, numbers = 2, special = 1, your response should be a password such as "D5%t9Bgf". Do not repeat the same password twice.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Welcome to password generator! Input the following: length = 8, capitalized = 1, lowercase = 5, numbers = 2, special = 1"
                initModel(template)
            case "english-translator":
                template="""I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. 
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "Translate any language into English!"
                initModel(template)
            case "travel-guide":
                template="""I want you to act as a travel guide. I will write you my location and you will suggest a place to visit near my location. In some cases, I will also give you the type of places I will visit. You will also suggest me places of similar type that are close to my first location.
                {history}
                Human: {input}
                AI:
                """
                st.session_state.infotext = "I am your travel guide, what city are you in?"
                initModel(template)

# streamlit text input
def get_text():
    input_text = st.text_input("Input Message: ", st.session_state.textbox, key="input")
    return input_text 

st.header(st.session_state.infotext)
user_input = get_text()

# state to hold generated output of llm
def memoryConversation(payload): 
    input = payload["inputs"]["text"]
    return st.session_state.conversation.predict(input=input)

# check if text input has been filled in
if user_input:
    # run langchain llm function returns a string as output
    output = memoryConversation({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },"parameters": {"repetition_penalty": 1.33},
    })

    # append user_input and output to state
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# If responses have been generated by the model
if st.session_state['generated']:
    # Reverse iteration through the list
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # message from streamlit_chat
        message(st.session_state["generated"][i], key=str(i), avatar_style="bottts")
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
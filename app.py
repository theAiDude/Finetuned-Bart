import streamlit as st
from transformers import BartForConditionalGeneration , BartTokenizer

# title
st.title("Finetunned Summarization Model")

# text input from user
text_input = st.text_area("Copy paste the text here...")
st.markdown("<br>" , unsafe_allow_html= True)
# Initialize model and tokenizer
model_path = "./tunned_bart"
model = BartForConditionalGeneration.from_pretrained(model_path)
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")

col1 , col2 , col3 = st.columns(3)

with col2:
    submit_btn = st.button("Summarize",use_container_width= True)

if submit_btn:

    # input vector embedding
    tokenized_input = tokenizer(text_inputw,max_length=1000 , return_tensors="pt",truncation = True , padding = "max_length")
    # output vector embedding
    tokenized_output = model.generate(tokenized_input["input_ids"] , max_length= 350 , early_stopping = True )
    # final response
    generated_summary = tokenizer.decode(tokenized_output[0] , skip_special_tokens= True)

    # display response
    st.info(generated_summary)
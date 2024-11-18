from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BERTSUM model and tokenizer
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def summarizer(text):
    # Tokenize and encode the text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    # Calculate lengths
    len_orig = len(text.split())
    len_summ = len(summary.split())
    
    return summary, text, len_orig, len_summ

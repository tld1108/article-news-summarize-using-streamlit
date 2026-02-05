from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text, max_length=100, min_length=30):
    input_text = f"summarize: {text}"
    
    inputs = tokenizer(
        input_text, 
        return_tensors="pt", 
        max_length=512, 
        truncation=True
    )
    
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
    
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

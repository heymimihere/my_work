from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

model_id = "/root/meta-llama/Meta-Llama-3-8B-Instruct"  # Base model directory

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)

# If you have fine-tuned Lora model, load it here
model = PeftModel.from_pretrained(model, "/root/my_work/sft")
model = model.merge_and_unload()

while True:
    # Start conversation
    messages = [
        {"role": "system", "content": "现在你是一个心理专家，我有一些心理问题，请你用专业的知识帮我解决。"},
    ]

    # Main conversation loop
    while True:
        # Get user input
        user_input = input("User: ")
        # Add user input to the conversation history
        messages.append({"role": "user", "content": user_input})

        # Convert conversation history to input_ids
        input_ids = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(model.device)

        # Generate response
        outputs = model.generate(
            input_ids,
            max_new_tokens=8196,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        response = outputs[0][input_ids.shape[-1]:].tolist()

        # Decode response and print
        print("Bot:", tokenizer.decode(response, skip_special_tokens=True))

        # Add bot response to conversation history
        messages.append({"role": "system", "content": tokenizer.decode(response, skip_special_tokens=True)})


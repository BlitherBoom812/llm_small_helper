import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com" 
os.environ['TRANSFORMERS_CACHE'] = os.environ['HF_DIR']
os.environ['CUDA_VISIBLE_DEVICES']='0,1,2,3,4,5,6,7'

hf_token = "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"

# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-alpha/", device_map='auto')
# print(pipe("", max_new_tokens=1000))

from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
model_name = "HuggingFaceH4/nworld/zephyr-7b-alpha"
# check_point = "HuggingFaceH4/zephyr-7b-alpha/checkpoint-1000"
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     device_map="auto",
#     token=hf_token,
#     force_download=True, 
#     resume_download=False
# )
# tokenizer = AutoTokenizer.from_pretrained(
#     model_name,
#     device_map="auto",
#     token=hf_token
# )

model = pipe.model

tokenizer = pipe.tokenizer

tokenizer.padding_side = 'right'

# data_dir = ""
# dataset_name = "BirdL/DONOTUSEDATA-SideB"

# from datasets import load_dataset
# dataset_path = None
# if data_dir == None:
#     dataset_path = dataset_name
# else:
#     dataset_path = os.path.join(data_dir, dataset_name)

# dataset = load_dataset(dataset_path)

data_dir = ""
dataset_name = "BirdL/DONOTUSEDATA-SideB"
from datasets import load_dataset
dataset = load_dataset(dataset_name)

def replace(example):
  remove_list = ['>', 'http:', "/", "\\", '.com']
  for remove_item in remove_list:
    example['text'] = example['text'].replace(remove_item, "")
  return example

dataset['train'] = dataset['train'].map(replace)

print(dataset['train'][0]['text'])

from peft import LoraConfig
from transformers import TrainerCallback

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

class PeftSavingCallback(TrainerCallback):
    def on_save(self, args, state, control, **kwargs):
        checkpoint_path = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
        kwargs["model"].save_pretrained(checkpoint_path)
        if "pytorch_model.bin" in os.listdir(checkpoint_path):
            os.remove(os.path.join(checkpoint_path, "pytorch_model.bin"))


save_name = "hello_wrokd"
from trl import SFTTrainer
from transformers import TrainingArguments

callbacks = [PeftSavingCallback()]

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset['train'],
    dataset_text_field="text",
    max_seq_length=512,
    peft_config=peft_config,
    callbacks=callbacks,
    args=TrainingArguments(
        num_train_epochs=20,
        output_dir=model_name,
        push_to_hub=False,
        hub_strategy="all_checkpoints",
        hub_token=hf_token
    )
)
trainer.train(resume_from_checkpoint=True)

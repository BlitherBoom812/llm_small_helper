import os

# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com" 
os.environ['TRANSFORMERS_CACHE'] = os.environ['HF_DIR']
os.environ['CUDA_VISIBLE_DEVICES']='0,1,2,3,4,5,6,7'

data_dir = ""
dataset_name = ""

from datasets import load_dataset
dataset = load_dataset(dataset_name)

def replace(example):
  remove_list = ['>', 'http:', "/", "\\", '.com']
  for remove_item in remove_list:
    example['text'] = example['text'].replace(remove_item, "")
  return example

dataset['train'] = dataset['train'].map(replace)

print(dataset['train'][0]['text'])

dataset.save_to_disk(dataset_dict_path=os.path.join(data_dir, dataset_name))
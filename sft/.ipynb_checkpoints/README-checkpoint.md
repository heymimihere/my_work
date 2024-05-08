---
license: other
library_name: peft
tags:
- llama-factory
- lora
- generated_from_trainer
base_model: /root/meta-llama/Meta-Llama-3-8B-Instruct
model-index:
- name: sft
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sft

This model is a fine-tuned version of [/root/meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co//root/meta-llama/Meta-Llama-3-8B-Instruct) on the data_pro_2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0449

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 20
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.3069        | 0.2963 | 100  | 1.2734          |
| 1.2042        | 0.5926 | 200  | 1.1648          |
| 1.1168        | 0.8889 | 300  | 1.1190          |
| 1.1041        | 1.1852 | 400  | 1.0927          |
| 1.0738        | 1.4815 | 500  | 1.0747          |
| 1.0479        | 1.7778 | 600  | 1.0609          |
| 1.0585        | 2.0741 | 700  | 1.0521          |
| 1.0289        | 2.3704 | 800  | 1.0474          |
| 1.0413        | 2.6667 | 900  | 1.0453          |
| 1.048         | 2.9630 | 1000 | 1.0449          |


### Framework versions

- PEFT 0.10.0
- Transformers 4.40.1
- Pytorch 2.3.0+cu121
- Datasets 2.18.0
- Tokenizers 0.19.1
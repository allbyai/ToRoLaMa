# Toro LLaMA: The Vietnamese Instruction-Following and Chat Model
**Authors**: **Duy Quang Do<sup>1</sup>**, **Hoang Le<sup>1</sup>** and **Duc Thang Nguyen<sup>2</sup>**<br>
<sup>1</sup>*Taureau AI, Hanoi, Vietnam*<br>
<sup>2</sup>*Torus AI, Toulouse, France*


Toro LLaMA is a collaborative effort between Taureau AI from Vietnam and Torus AI from France. It stands as an open-source, multi-turn, large language model (LLM), initially crafted with a focus on the Vietnamese language. It represents the first step towards a wider goal of supporting a variety of languages, particularly those relevant to Torus' array of products.  Developed using a diverse and extensive dataset, Toro-LLaMA aims to provide an enhanced understanding and representation of languages, aspiring to meet and possibly exceed the efficiency, performance, and commercial applicability of existing LLMs.

This release includes the model weights, inference code, and evaluation results for the 7B (7-billion parameter) version, initially focused on Vietnamese, with forthcoming adaptations for additional languages.

- [Introduction](#introduction)
- [Model weights](#model-weights)
- [Technical overview](#technical-overview)
- [Evaluations](#evaluations)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Acknowledgement](#acknowledgement)

## Introduction

Established in 2019, Torus Actions SAS, Toulouse, France (also known as [Torus AI](https://www.torus.ai)) was initiated by a collective of scientists under the leadership of Professor [Nguyen Tien Zung](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Ti%E1%BA%BFn_D%C5%A9ng), who discovered the toric conservation principle. This principle states that:
```
Everything conserved by a dynamical system is also conserved by its associated torus actions.
```

Taureau AI, set up in 2021 in Hanoi, is dedicated to pushing the frontiers of AI technology, focusing specifically on AI product engineering and software development. The company aims to contribute to the advancement of AI and software engineering within the Torus ecosystem.

Our objective is to create augmented intelligence solutions that contribute to the betterment of global well-being.

Toro-LLaMA, debuting with a focus on the Vietnamese language, is the initial step towards a versatile, multilingual platform. Designed for ease of deployment and functionality, and maintaining an open license, this model is intended to foster community engagement in addressing global challenges and promoting AI advancement.

## Model weights

Our lastest weights for Toro-LLaMA release can be found here:

| Date  | Version | Huggingface Repo | Context Length |
| ------------- | ------------- |------------- |------------- |
| 19/12/2023  | ```Toro-LLaMA-7B-1.0```  |[Toro-LLaMA 7B 1.0](https://huggingface.co/allbyai/ToroLLaMA-7b-v1.0) | 2048 |


## Technical overview

The pre-trained model is based on LLaMA 2 which fine-tuned on large raw dataset by bkai-foundation-labs [Vietnamese-LLaMA2](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB).

This mode, trained on 430k of high-quality, multi-turn conversation data, sourced from both open-source and in-house datasets, Toro LLaMA excels in chat modeling and Vietnamese language understanding. Sources include [UIT-ViQUAD](https://paperswithcode.com/dataset/uit-viquad), [Bactrian-X](https://huggingface.co/datasets/MBZUAI/Bactrian-X), [Grade-school-math](https://github.com/openai/grade-school-math),... Other datasets contain our custom conversation data and data covering multiple topics.

Key advantages of Toro-LLaMA include:

- Comprehensive open-source availability under the [LLaMA 2 LICENSE](https://github.com/facebookresearch/LLaMA)
- Enhanced speed with the [Vietnamese Tokenizer](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB) (Which about 1/4 less token in an Vietnamese sentence compared to ChatGPT and LLaMA), and a smaller model size.
- Superior performance over existing open-source models.
- Simplified deployment for a wide array of applications.

With Toro LLaMA, we hope to push the state of current AI technology huge step forward for Vietnam and Vietnamese people.

## Evaluations

Thank to the effort of [PhoGPT team](https://github.com/VinAIResearch/PhoGPT), we used the Vicuna translated benchmark question [HERE](https://docs.google.com/spreadsheets/d/122ldeXuBmLSFFqaFbflj82VyYTKL-Qc2hZiTI9csc-Q/edit#gid=44668470) with our benchmark results on **Toro-LLaMA**, and compared them using the [Fastchat MT-bench method](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge). The table bellow shows that **Toro-LLaMA** performs competitively against state-of-the-art models like ChatGPT.


The Fastchat benchmark method, used for evaluating language models, primarily focuses on the accuracy of information in responses. However, an important aspect not accounted for in this method is the right language accuracy. Both **URA-LLaMA-7B** and **URA-LLaMA-13B** often respond in English to Vietnamese questions. Realistically, their performance might be rated significantly lower when specifically benchmarked for proficiency in the Vietnamese language.

The average result shown in the table bellow:

Ranking | model          | Result   |
| ------------- | ------------- | ------------- |
1|gpt-4          |      9.52500 |
2|gpt-3.5-turbo         |     9.23750   |
3|**Toro-LLaMA 7B**         |    7.31875   |
4|URA-LLaMA-13B*     |   6.98750   |
5|PhoGPT-7B5-Instruct|  6.49375   |
6|Vietcuna-7B-v3      | 5.21250   |
7|URA-LLaMA-7B*       |  3.58750   |
8|Vietcuna-3B        |  2.28750   |

*: *URA's model real score must be much lower in the respect to Vietnamese answer quality evaluation*

The details of benchmark in term of subject is shown in the figure bellow (we do not display URA-LLaMA because they generate half of answer in english):

![Result](imgs/result.png)

**Toro-LLaMA 7B** excels in qualitative tasks compared to other model, particularly with its ability to write and answer almost on par with the GPT-3.5-turbo model. However, it shows limitations in quantitative tasks like coding and mathematics due to the nature of its training data. This suggests opportunities for future enhancements in STEM-related tasks.

For detailed benchmark information and to rerun the evaluation code, refer to  [Fastchat MT-bench method](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge). We have included the answers from each model, the prompts, and the evaluation results [HERE](https://huggingface.co/allbyai/torusgpt-7b-v1.0/tree/main/mt_bench) for reproduction. The generated results can also be accessed [HERE](https://docs.google.com/spreadsheets/d/1S1UmfImrLKFtxRmdX6B5plnIIyh3RiOr/edit?usp=sharing&ouid=102198682273617686649&rtpof=true&sd=true) for human evaluation.

## Run the model

Toro-LLaMA utilizes a prompt format similar to Vicuna,designed for multi-turn, high-speed, and token-efficient conversations. An example prompt is described bellow for illustration.

```
Cuộc hội thoại giữa người dùng và một trí thông minh nhân tạo. Đưa ra câu trả lời chính xác, giúp ích cho người dùng.

USER: Xin chào!
ASSISTANT: Xin chào!</s>
USER: Bạn khỏe chứ?
ASSISTANT: Tôi khỏe, cảm ơn.</s>
```

This template can be employed to operate the model via Huggingface transformers. The necessary inference code is available in the file [inference_hf.py](/inference_hf.py). Execute it using the following command:

```
python inference_hf.py
```

## Deployment

Toro-LLaMA can be easily deployed using Fastchat.

Step 1: Install fastchat
```
pip3 install "fschat[model_worker,webui]"
```

Step 2: Run the RESTful API Server

Begin by running the controller:
```
python3 -m fastchat.serve.controller
```

Next, launch the model worker:
```
python3 -m fastchat.serve.model_worker --model-path path-to-Toro-LLaMA --conv-template vicuna_v1.1
```

Then, initiate the RESTful API server:
```
python3 -m fastchat.serve.openai_api_server --host localhost --port 8000
```

Finaly, run the example streamlit code:
```
streamlit run demo.py
```

## License
Toro-LLaMA is licensed under the [Toro-LLaMA community License](/LICENSE) agreement.

Toro-LLaMA is licensed under the [LLaMA 2 Community License](https://ai.meta.com/LLaMA/license/), Copyright © Meta Platforms, Inc. All Rights Reserved.

## Disclaimer
This project (and its derivative works) is derived from Meta's LLaMA-2 model, and therefore strictly complies with the LLaMA 2 Community License Agreement. We explicitly declare that we offer no assurances, guarantees, or warranties about the accuracy, reliability, and/or completeness of the model's outputs or the data presented therein. We disclaim all liability for any immediate or subsequent losses, damages, consequences, or implications arising from the models. Please be aware that the model's generated content might include inaccuracies, profanity, hate speech, discriminatory remarks, and/or misleading narratives. Using these models for commercial purposes requires full compliance with all applicable local laws and regulations to verify the legality of the content produced by the model. This project holds no accountability for any products or services that are developed utilizing its resources.

## Acknowledgement

Special thanks to [bkai-foundation-labs](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB), [phogpt](https://github.com/VinAIResearch/PhoGPT), and [fastchat](https://github.com/lm-sys/FastChat/tree/main) for their contributions and references in our work.

Please consider citing our work if you find the Toro LLaMA beneficial.

```
@misc{allbyai2023toroLLaMA,
    title={Toro-LLaMA: The Vietnamese Instruction-Following and Chat Model},
    author={Duy Quang Do, Hoang Le and Duc Thang Nguyen},
    year={2023},
    note={https://github.com/allbyai/ToroLLaMA}
    howpublished={Software}
}
```

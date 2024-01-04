# ToRoLaMa: The Vietnamese Instruction-Following and Chat Model
**Authors**: **Duy Quang Do<sup>1</sup>**, **Hoang Le<sup>1</sup>** and **Duc Thang Nguyen<sup>2</sup>**<br>
<sup>1</sup>*Taureau AI, Hanoi, Vietnam*<br>
<sup>2</sup>*Torus AI, Toulouse, France*

<p align="center" width="100%">
  <img src="imgs/ToRoLaMa.png" width="45%"/>
</p>

ToRoLaMa is the result of a collaborative effort of Vietnam-based Taureau AI and France-based Torus AI. It stands as an open-source, multi-turn, large language model (LLM), initially created with a focus on the Vietnamese language. It represents the first step towards a wider goal of supporting a variety of international languages.

- [Introduction](#introduction)
- [Model weights](#model-weights)
- [Technical overview](#technical-overview)
- [Evaluations](#evaluations)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Acknowledgement](#acknowledgement)

## Introduction

[Torus AI](https://www.torus.ai) (official name: Torus Actions SAS) was founded in Toulouse (France) in 2019 by a group of scientists under the leadership of [Nguyen Tien Zung](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Ti%E1%BA%BFn_D%C5%A9ng), distinguished professor of mathematics at the University of Toulouse. The name Torus Actions comes from *the toric conservation principle* discovered by Zung:
```
Everything conserved by a dynamical system is also conserved by its associated torus actions.
```

[Taureau AI](https://www.taureau.ai), set up in 2021 in Hanoi by Torus AI people, is focused on the development of a general-purpose AI platform, AI product engineering and software development, to serve the other companies inside and outside the Torus AI ecosystem.

Our common objective is to create augmented intelligence solutions that serve millions of people and make the world a happier place.

Our large language model - ToRoLaMa, developed using a diverse and extensive dataset, aims to provide an enhanced understanding and representation of languages, aspiring to meet and possibly exceed the efficiency, performance, and applicability of existing commercial LLMs.

With ToRoLaMa, we hope to contribute to the rapid progress in language processing for Vietnamese speaking people and applications.We also plan to extend it (and other LLMs) to other languages.

This release includes the model weights, inference code, and evaluation results for the 7B (7 billion parameter) version.

## Model weights

Our lastest weights for ToRoLaMa can be found here:

| Date  | Version | Huggingface Repo | Context Length |
| ------------- | ------------- |------------- |------------- |
| 19/12/2023  | ```ToRoLaMa-7B-1.0```  |[ToRoLaMa 7B 1.0](https://huggingface.co/allbyai/ToRoLaMa-7b-v1.0) | 2048 |


## Technical overview
The ToRoLaMa's pre-trained model is based on [Vietnamese-LLaMA2](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB), a fine-tuned version of LLaMA 2 model provided by bkai-foundation-labs, enhanced with a large Vietnamese-language dataset. The model then was trained using 430K high-quality, multi-turn questions/answers. Data sources for the training include [UIT-ViQUAD](https://paperswithcode.com/dataset/uit-viquad), [Bactrian-X](https://huggingface.co/datasets/MBZUAI/Bactrian-X), [Grade-school-math](https://github.com/openai/grade-school-math), etc and our in-house data that contain conversations on multiple topics.

Key advantages of ToRoLaMa include:

- Open-source availability under the [LLaMA 2 License](https://github.com/facebookresearch/LLaMA)
- Enhanced speed with a smaller model size and an innovative [Vietnamese Tokenizer](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB), whose tokens are 25% shorter compared to ChatGPT and LLaMA for Vietnamese phrases.
- Superior performance over existing open-source models (see benchmark results below).
- Simplified deployment for a wide range of applications.

## Evaluations

We used benchmark results of [Vicuna and PhoGPT](https://docs.google.com/spreadsheets/d/122ldeXuBmLSFFqaFbflj82VyYTKL-Qc2hZiTI9csc-Q/edit#gid=44668470) to evaluate ToRoLaMa and compared our results with others using the [Fastchat MT-bench method](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge). The table below shows that **ToRoLaMa** performs competitively against state-of-the-art models like ChatGPT.

The Fastchat benchmark method, used for evaluating language models, primarily focuses on the accuracy of information in responses. However, an important aspect not accounted for in this method is the accuracy in the choice of language (English vs. Vietnamese). Both **URA-LLaMA-7B** and **URA-LLaMA-13B** often respond in English to Vietnamese questions. Their performance may be rated much lower when specifically benchmarked for proficiency in Vietnamese.

The benchmark scores are shown in the following table:

Ranking | Model          | Score   |
| ------------- | ------------- | ------------- |
1|gpt-4          |      9.52500 |
2|gpt-3.5-turbo         |     9.23750   |
3|**ToRoLaMa 7B**         |    7.31875   |
4|URA-LLaMA-13B*     |   6.98750   |
5|PhoGPT-7B5-Instruct|  6.49375   |
6|Vietcuna-7B-v3      | 5.21250   |
7|URA-LLaMA-7B*       |  3.58750   |
8|Vietcuna-3B        |  2.28750   |

*: *The scores of URA models here do not take into account the fact that they often answer in English to questions posed in Vietnamese.*

The details of benchmark in terms of subjects are shown in the following figure (we do not display URA-LLaMA because they generate half of the answers in English):

![Result](imgs/result.png)

The above benchmark results show that **ToRoLaMa** excels in qualitative tasks compared to the other models, particularly with its ability to write and answer almost on par with GPT-3.5-turbo. However, it shows limitations in quantitative tasks like coding and mathematics due to the nature of its training data. This suggests opportunities for future improvements in STEM-related tasks.

For detailed benchmark information and to rerun the evaluation code, refer to  [Fastchat MT-bench method](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge). We have included the answers from each model, the prompts, and the evaluation results [HERE](https://huggingface.co/allbyai/ToRoLaMa-7b-v1.0/tree/main/mt_bench) for reproduction. The generated results can also be accessed [HERE](https://docs.google.com/spreadsheets/d/1S1UmfImrLKFtxRmdX6B5plnIIyh3RiOr/edit?usp=sharing&ouid=102198682273617686649&rtpof=true&sd=true) for human evaluation.

## Run the model

ToRoLaMa uses a prompt format similar to Vicuna, designed for multi-turn, high-speed, and token-efficient conversations. An example prompt is shown below for illustration.

```
Cuộc hội thoại giữa người dùng và một trí thông minh nhân tạo. Đưa ra câu trả lời chính xác, giúp ích cho người dùng.

USER: chào
ASSISTANT: Xin chào! Tôi có thể giúp gì cho bạn hôm nay?</s>
USER: để quản lý thời gian hiệu quả tôi nên làm thế nào??
ASSISTANT: Để quản lý thời gian hiệu quả, bạn có thể thực hiện các bước sau đây:

    Lập kế hoạch: Tạo ra lịch trình hoặc danh sách công việc cần làm trong ngày hoặc tuần.

    Ưu tiên công việc: Xác định công việc quan trọng và ưu tiên thực hiện trước.

    Sử dụng lịch: Sử dụng lịch để theo dõi các hoạt động và sự kiện trong ngày.

    Sử dụng một số công cụ hỗ trợ: Sử dụng các công cụ trực tuyến, ứng dụng điện thoại di động để giúp quản lý thời gian.

    Tránh phân tâm: Tránh những việc phức tạp và không cần thiết để giải quyết trong quá trình làm việc.

    Nghỉ ngơi: Để giảm căng thẳng và tăng năng suất, hãy dành thời gian nghỉ ngơi giữa các công việc.

    Đánh giá và cải tiến: Đánh giá các phương pháp quản lý thời gian của bạn để tìm cách cải tiến trong tương lai.

Những cách trên sẽ giúp bạn quản lý thời gian hiệu quả hơn và tăng cường năng suất trong công việc.</s>
```

The file [inference_hf.py](/inference_hf.py) in our github repository contains an example code for running ToRoLaMa model from Huggingface hub. Execute it using the following command:

```
python inference_hf.py
```

## Deployment

ToRoLaMa can be easily deployed using Fastchat.

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
python3 -m fastchat.serve.model_worker --model-path path-to-ToRoLaMa --conv-template vicuna_v1.1
```

Then, initiate the RESTful API server:
```
python3 -m fastchat.serve.openai_api_server --host localhost --port 8000
```

Finally, run the example streamlit code:
```
streamlit run demo.py
```

## License
ToRoLaMa is licensed under the [ToRoLaMa community License](/LICENSE) agreement.

ToRoLaMa is licensed under the [LLaMA 2 Community License](https://ai.meta.com/LLaMA/license/), Copyright © Meta Platforms, Inc. All Rights Reserved.

## Disclaimer
This model is derived from Meta's LLaMA-2 model, and therefore strictly complies with the LLaMA 2 Community License Agreement. We explicitly declare that we offer no assurances, guarantees, or warranties about the accuracy, reliability, usability, or completeness of the model's outputs or the data presented therein. We disclaim all liability for any immediate or subsequent losses, damages or adverse consequences arising from the use of our model. Please be aware that the model's generated content might include inaccuracies, profanity, hate speech, discriminatory remarks, and/or misleading narratives. Using this model or its derivatives for commercial purposes requires full compliance with all applicable local laws and regulations regarding the legality of the content produced by the model. We hold no accountability for any products or services that are developed using ToRoLaMa and its related files.

## Acknowledgement

The [bkai-foundation-labs](https://huggingface.co/bkai-foundation-models/vietnamese-LLaMA2-7b-40GB), [phogpt](https://github.com/VinAIResearch/PhoGPT), and [fastchat](https://github.com/lm-sys/FastChat/tree/main) and references therein have been used in this work.

In case you use ToRoLaMa, please cite our work in your publications :

```
@misc{allbyai2023ToRoLaMa,
    title={ToRoLaMa: The Vietnamese Instruction-Following and Chat Model},
    author={Duy Quang Do, Hoang Le and Duc Thang Nguyen},
    year={2023},
    note={https://github.com/allbyai/ToRoLaMa}
    howpublished={Software}
}
```

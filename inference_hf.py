# author: AllByAI, TorusAI
# this software is licensed under the Toro-LlaMA License and Llama2.

import torch
import transformers

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_path = "allbyai/ToroLLaMA-7b-v1.0"

model = transformers.AutoModelForCausalLM.from_pretrained(model_path,
                                                          torch_dtype=torch.float16)

tokenizer = transformers.AutoTokenizer.from_pretrained(model_path,
                                                       use_fast=True)
model.eval()

PROMPT_TEMPLATE = """Cuộc hội thoại giữa người dùng và một trí thông minh nhân tạo. Đưa ra câu trả lời chính xác, giúp ích cho người dùng.

USER: {question}
ASSISTANT:"""

question = "Nêu cách để quản lý thời gian hiệu quả."
input_prompt = PROMPT_TEMPLATE.format(question=question)
input_ids = tokenizer(input_prompt, return_tensors="pt").to(device)
model = model.to(device)
outputs = model.generate(
    inputs=input_ids["input_ids"],
    attention_mask=input_ids["attention_mask"],
    do_sample=True,
    temperature=1.0,
    top_k=50,
    top_p=0.9,
    max_new_tokens=2048,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.pad_token_id
)

response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
response = response.split("ASSISTANT:")[1]
print(response)

# Để quản lý thời gian hiệu quả, bạn có thể thực hiện các bước sau đây:

# 1. Lập danh sách công việc: Hãy lập danh sách các công việc cần làm trong ngày hoặc tuần đó. Việc này sẽ giúp bạn có thể lên kế hoạch và hiểu rõ những việc cần làm gì.

# 2. Ưu tiên công việc: Sau khi lập danh sách công việc, bạn cần phải đánh giá mức độ ưu tiên cho từng công việc. Hãy bắt đầu với những công việc quan trọng và khó khăn nhất.

# 3. Đặt mục tiêu cụ thể: Hãy đặt mục tiêu cụ thể cho từng công việc. Việc này sẽ giúp bạn có thể đạt được những kết quả mong muốn và quản lý thời gian tốt hơn.

# 4. Sử dụng lịch: Sử dụng lịch để lên kế hoạch cho các công việc. Lịch giúp bạn có thể theo dõi các hoạt động và sự kiện trong ngày và tuần.

# 5. Cố định thời gian: Cố định thời gian cho từng công việc. Việc này sẽ giúp bạn có thể quản lý tốt thời gian và hoàn thành công việc quan trọng và khó khăn nhất trước khi quá trễ.

# 6. Tập trung vào công việc: Không để bất kỳ sự phân tâm nào ảnh hưởng đến công việc. Hãy tập trung vào từng nhiệm vụ và hoàn thành nó một cách kỹ lưỡng.

# 7. Nghỉ ngơi đầy đủ: Để giữ cho sức khỏe và tinh thần tốt, bạn cần phải nghỉ ngơi đầy đủ trong ngày và tuần đó.

# 8. Cập nhật danh sách công việc: Luôn cập nhật danh sách công việc để đảm bảo bạn không bỏ lỡ bất kỳ công việc nào và có thể điều chỉnh kế hoạch nếu cần thiết.

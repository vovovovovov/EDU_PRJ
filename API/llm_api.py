# 暂时先调用讯飞星火模型进行测试
import time
import json
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from pprint import pprint

#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = '6c4adba5'
SPARKAI_API_SECRET = 'NGUyZmIyZjUyNDY2Y2I5NzU5ZDI4MTll'
SPARKAI_API_KEY = 'bc855be4307e0aed9a31e51297b14825'
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'


# api接口
def llm_api(question):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content= question
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    return a.generations[0][0].text
    # return json.loads(a.generations[0][0].text)

# 用单纯的step_by_step的coT达到类似o1模型的效果
def answer_step_by_step(question):
    messages = [
        {"role": "system", "content": """You are an expert AI assistant that 
        explains your reasoning step by step. For each step, provide a title 
        that describes what you're doing in that step, along with the content. 
        Decide if you need another step or if you're ready to give the final answer. 
        Respond in JSON format with 'title', 'content', and 'next_action' (either 'continue' or 'final_answer') keys.
        USE AS MANY REASONING STEPS AS POSSIBLE. AT LEAST 3. BE AWARE OF YOUR LIMITATIONS AS AN LLM AND WHAT YOU CAN
        AND CANNOT DO. IN YOUR REASONING, INCLUDE EXPLORATION OF ALTERNATIVE ANSWERS. CONSIDER YOU MAY BE WRONG, AND
        IF YOU ARE WRONG IN YOUR REASONING, WHERE IT WOULD BE. FULLY TEST ALL OTHER POSSIBILITIES. YOU CAN BE WRONG.
        WHEN YOU SAY YOU ARE RE-EXAMINING, ACTUALLY RE-EXAMINE, AND USE ANOTHER APPROACH TO DO SO. DO NOT JUST SAY YOU 
        ARE RE-EXAMINING. USE AT LEAST 3 METHODS TO DERIVE THE ANSWER. USE BEST PRACTICES.

        Example of a valid JSON response:
        ```json
        {
            "title": "Identifying Key Information",
            "content": "To begin solving this problem, we need to carefully examine the 
            given information and identify the crucial elements that will guide our solution process. 
            This involves...",
            "next_action": "continue"
        }```
        """},
        {"role": "user", "content": question},
        {"role": "assistant", "content": "Thank you! I will now think step by step following my instructions, starting at the beginning after decomposing the problem."}
    ]

    # 记录思维步骤
    steps = []
    step_count = 1
    total_thinking_time = 0  # 总思考时间

    while True:
        start_time = time.time()
        step_data = llm_api(messages)
        end_time = time.time()
        thinking_time = end_time - start_time
        total_thinking_time += thinking_time

        steps.append((f"Step {step_count}: {step_data['title']}", step_data['content'], thinking_time))

        messages.append({"role": "assistant", "content": json.dumps(step_data)})

        if step_data['next_action'] == 'final_answer' or step_count > 25:  # Maximum of 25 steps to prevent infinite thinking time. Can be adjusted.
            break

        step_count += 1

        # 使用yield生成器冻结当前状态
        yield steps, None

    # 生成最终结果
    messages.append({"role": "user", "content": "Please provide the final answer based on your reasoning above."})

    start_time = time.time()
    final_data = llm_api(messages)
    end_time = time.time()
    thinking_time = end_time - start_time
    total_thinking_time += thinking_time

    steps.append(("Final Answer", final_data['content'], thinking_time))

    yield steps, total_thinking_time

def test_step_by_step():
    user_query = "1+1=?"
    # Generate and display the response
    for steps, total_thinking_time in answer_step_by_step(user_query):
        for i, (title, content, thinking_time) in enumerate(steps):
            if title.startswith("Final Answer"):
                print(f"{i}. {title}: {content}")
            else:
                print("not final answer")
                print(f"{i}. {title}: {content}")

        # Only show total time when it's available at the end
        if total_thinking_time is not None:
            print(f"{total_thinking_time}")


if __name__ == '__main__':
    test_step_by_step()
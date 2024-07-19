# agent入口

"""
todo:
    1.加载环境变量
    2.工具的引入
    3.prompt模板
    4.模型的初始化
"""
import time
from tools.tools import tools_map
from prompt import generate_prompt


# 参数解析
def parse_thoughts(response):
    """
           response:
           {
               "action":{
                   "name": "action name",
                   "args":{
                           "args name": "args value",
                       }
                   }
               "thoughts":{
                   "text" : "thought",
                   "plan": "plan",
                   "criticism": "criticism",
                   "speak": "当前步骤返回给用户的总结",
                   "reasoning": "reasoning",
                   }
           }
           """
    try:
        thoughts = response.get("thoughts")
        observation = thoughts.get("speak")
        plan = thoughts.get("plan")
        reasoning = thoughts.get("reasoning")
        criticism = thoughts.get("criticism")
        prompt = f"plan:{plan}\n reasoning: {reasoning}\n criticism: {criticism}\n observation: {observation}"
        return prompt
    except Exception as e:
        print("发生错误: " , e)
        return "".format(e)

def agent_execute(query, max_request_time=10):
    cur_request_tiem = 0
    # TODO 记忆功能,可以用时间戳优化，可以划分长短期记忆
    chat_history = []
    agent_scrach = ''
    while cur_request_tiem < max_request_time:
        cur_request_tiem = cur_request_tiem + 1
        """
        如果返回结果达到预期，则返回
        """
        # prompt功能：1.任务描述 2.工具描述 3.用户输入（user_msg） 4.assistant_msg  5.限制 6.更好的实践描述
        prompt = generate_prompt(query, agent_scrach)
        start_time = time.time()
        print("****************{},开始调用大模型...".format(cur_request_tiem),flush=True)
        # TODO 大模型调用
        response = call_llm()
        end_time = time.time()
        print("****************{},大模型调用结束，耗时：{}.....".format(cur_request_tiem,end_time-start_time),flush=True)

        if not response or not isinstance(response,dict):
            print("调用大模型错误，即将重试...",response)
            continue
        """
        response:
        {
            "action":{
                "name": "action name",
                "args":{
                        "args name": "args value",
                    }
                }
            "thoughts":{
                "text" : "thought",
                "plan": "plan",
                "criticism": "criticism",
                "speak": "当前步骤返回给用户的总结",
                "response": "response",
                }
        }
        """
        action_info = response.get("action")
        action_name = action_info.get("name")
        action_args = action_info.get("args")
        print("当前action: ",action_name,action_args)

        if action_name == "finish":
            final_answer = action_args.get("answer")
            print("最终结果: ", final_answer)
            break
        observation = response.get("thoughts").get("speak")
        try:
            """
                action_name到函数的一个映射
            """
            tools_map = tools_map
            func = tools_map.get(action_name)
            observation = func(**action_args)

        except Exception as e:
            print("调用工具异常: ",e)
        agent_scrach = agent_scrach + "\n" + observation

        user_msg = "决定使用哪个工具"
        assisant_msg = parse_thoughts(response)




def main():
    #需求：支持用户的多次交互
    max_request_time = 10 # 最多请求次数
    while True:
        query = input("输入你的目标")
        if query == "exit":
            return

if __name__ == '__main__':
    print("begin")
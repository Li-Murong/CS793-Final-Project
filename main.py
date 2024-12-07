from agent import Agent
from agent import Judger


def main():
    user_question = input("Please input your question: ")

    QAs = {"question": user_question}

    openai_agent = Agent("openai")
    llama_agent = Agent("llama")

    print("Calling OpenAI:")
    openai_response = openai_agent.get_answer(user_question)
    QAs["openai"] = openai_response
    print(f"OpenAI Response: {openai_response}")

    print("\nCalling LLaMA:")
    llama_response = llama_agent.get_answer(user_question)
    QAs["llama"] = llama_response
    print(f"LLaMA Response: {llama_response}")

    def mutual_analysis(QAs):
        openai_prompt = f"question: {QAs['question']}. response:{QAs['llama']}.evaluate the response to the question. Give a score of 1-10."

        llama_prompt = f"question: {QAs['question']}. response:{QAs['openai']}.evaluate the response to the question. Give a score of 1-10."

        openai_analysis = openai_agent.get_answer(openai_prompt)
        llama_analysis = llama_agent.get_answer(llama_prompt)

        print(f"\nOpenAI Analysis of Llama's response: {openai_analysis}")
        print(f"\nLlama Analysis of OpenAI's response: {llama_analysis}")

    mutual_analysis(QAs)

    judger = Judger()

    best_response = judger.get_best_response(QAs)

    print("\n=== Best Response ===")
    print(best_response)


if __name__ == "__main__":
    main()

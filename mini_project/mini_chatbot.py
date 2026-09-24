from ollama import chat

system_msg = "you are a friendly author. Answer in friendly.Anuswer in one line only."
history = [{"role" : "system","content" : system_msg}]
question_counter =0
while True:
    question = input("you:")
    if question == " ":
        print("SIRI 🤖:please type something.")
        continue
    if question.lower().strip() == "/history":
        print("------- Your conversation so far -------")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg['role'] == "user":
                speaker = "You"
            else:
                speaker = "SIRI 🤖"
            print(f"{speaker}: {msg['content']}")
        print("----------------------------")
        print()
        continue
    if question.lower().strip() == "/clear":
        history = [{"role" : "system","content" : system_msg}]
        print("Conversation cleared.")
        print()
        continue
    if question.lower().strip() == '/help':
        print("------- Available commands ---------")
        print("/history - display conversation history")
        print("/clear - clear chat history")
        print("/help - display this list")
        print("exit - quits the chatbot")
        print("------------------------------------")
        print()
        continue
    if question.lower().strip() == "exit":
        print("SIRI 🤖: Goodbye user.please come back soon!")
        print(f"You asked {question_counter} questions today.Good job!!")
        break
    history.append({"role" : "user","content" : question})
    question_counter += 1
    try:
        response = chat(
            model="llama3.2",
            messages = history 
        )

        reply = response.message.content
        history.append({"role" : "assistant","content" : reply})
        print(f"SIRI 🤖 :{reply}")
        print()
        print("---------------------------------------------------")
        print()
    except Exception as e:
        print("Unknown issue. Is ollama running?")
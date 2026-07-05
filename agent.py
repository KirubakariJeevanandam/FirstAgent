class MyAgent:
  def __init__(self):
    self.memory = []
    self.state = "idle"
  def act(self,input_text)"
    self.memory.append(input_text)
    return f"Agent Received: {input_text}"

if __name__ == "__main__":
    agent = MyAgent()
    print(agent.act("Hello from GitHub Codespaces!"))

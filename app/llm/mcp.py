from llama_cpp import Llama

llm = Llama(
  model_path="./app/llm/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
  n_ctx=2048,
  n_threads=8,
)

class MCPAgent:
  def __init__(self, system_prompt: str = "You are a developer's rubber duck and helpful assistant. Your job is only to help rubber duck and debug code."):
    self.llm = llm
    self.system_prompt = system_prompt
    self.chat_history = []

  def ask(self, user_input: str) -> str:
    self.chat_history.append({"role": "user", "content": user_input})
    prompt = self._build_prompt()
    result = self.llm(prompt, max_tokens=200, stop=["</s>"])
    response = result["choices"][0]["text"].strip()
    self.chat_history.append({"role": "assistant", "content": response})
    return response

  def _build_prompt(self) -> str:
    lines = [self.system_prompt, ""]
    for turn in self.chat_history:
      prefix = "User" if turn["role"] == "user" else "Assistant"
      lines.append(f"{prefix}: {turn['content']}")
    lines.append("Assistant:")
    return "\n".join(lines)

  def reset(self):
    self.chat_history = []
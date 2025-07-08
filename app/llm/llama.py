from llama_cpp import Llama

llm = Llama(
  model_path="./app/llm/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
  n_ctx=2048,
  n_threads=8,
)

def ask(prompt: str) -> str:
    result = llm(prompt, max_tokens=200, stop=["</s>"])
    print(result["choices"][0]["text"].strip())
    return result["choices"][0]["text"].strip()
from my_ai_project.config import LLMConfig
from my_ai_project.clients.anthropic import AnthropicClient
from my_ai_project.retrieval.chunker import chunk_text
import my_ai_project.retrieval.embedder as embedder


config = LLMConfig(
    model="claude-sonnet-4-5",
    temperature=0.3,
    system_prompt="You are a concise Python tutor.",
)

print(config)
print(config.as_dict)

chunks = list(chunk_text("hello world this is Python", chunk_size=2))
print(chunks)

vectors = embedder.embed_texts(["hello", "world"])
print(vectors)

client = AnthropicClient("dummy-key")
print(client.generate("Hello"))
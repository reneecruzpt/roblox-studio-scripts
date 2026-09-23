import requests, time

start = time.time()

r = requests.post("http://localhost:11434/api/generate", json={
    "model": "deepseek-r1:32b",
    "prompt": "Write 5 facts about ancient Rome. Be detailed.",
    "stream": False,
})

elapsed = time.time() - start
data = r.json()

tokens = data.get("eval_count", 0)
duration = data.get("eval_duration", 1) / 1e9  # nanoseconds → seconds

print(f"Tokens gerados: {tokens}")
print(f"Tempo: {elapsed:.1f}s")
print(f"Tokens/segundo: {tokens/duration:.1f}")
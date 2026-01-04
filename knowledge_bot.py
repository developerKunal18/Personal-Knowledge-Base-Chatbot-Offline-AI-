import re
from collections import defaultdict

knowledge = {}

def load_notes():
    print("Paste your notes (type END to finish):")
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        for sentence in re.split(r'[.!?]', line):
            words = sentence.lower().split()
            for word in words:
                knowledge.setdefault(word, []).append(sentence.strip())

def ask():
    while True:
        q = input("\nAsk a question (or 'exit'): ").lower()
        if q == "exit":
            break

        for word in q.split():
            if word in knowledge:
                print("📚", knowledge[word][0])
                break
        else:
            print("🤔 I don't know that yet.")

print("🤖 Knowledge Bot\n")
load_notes()
ask()

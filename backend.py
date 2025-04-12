# backend.py
import spacy

class CLATBot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.nlp = spacy.load("en_core_web_md")

    def get_best_match(self, query: str) -> str:
        query_doc = self.nlp(query)
        best_score = 0
        best_answer = "❓ Sorry, I couldn't find an answer for that. Try rephrasing your question."
        
        for key, answer in self.knowledge_base.items():
            key_doc = self.nlp(key)
            score = query_doc.similarity(key_doc)
            if score > best_score:
                best_score = score
                best_answer = answer

        return best_answer

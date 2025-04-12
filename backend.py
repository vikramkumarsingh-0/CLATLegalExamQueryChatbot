
from sentence_transformers import SentenceTransformer, util

class CLATBot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        
        self.keys = list(knowledge_base.keys())
        self.embeddings = self.model.encode(self.keys, convert_to_tensor=True)

    def get_best_match(self, query: str) -> str:
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        
        scores = util.cos_sim(query_embedding, self.embeddings)[0]

       
        best_idx = scores.argmax().item()
        best_score = scores[best_idx].item()

        
        if best_score < 0.4:
            return "Sorry, I couldn't find an answer for that. Try rephrasing your question."

        best_key = self.keys[best_idx]
        return self.knowledge_base[best_key]

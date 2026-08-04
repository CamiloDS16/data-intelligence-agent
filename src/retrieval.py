from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = start + chunk_size - overlap
    return chunks


def embed_texts(texts):
    embeddings = model.encode(texts)
    return embeddings


def search(query, text, top_n=3):
    chunks = chunk_text(text)
    chunks_emb = (embed_texts(chunks))
    query_embeddings = (embed_texts([query]))
    #calculating cosine similarity scores
    cosine_scores = cosine_similarity(query_embeddings, chunks_emb)[0]
    # pairing chunks with their respective score
    scored_chunks = list(zip(chunks, cosine_scores))
    # time complexity - first sorting: sort by the score, second item in each pair ([1]), highest first (reverse=True)
    scored_chunks.sort(key=lambda pair:pair[1], reverse=True)
    # returns top_n
    return [chunk for chunk, score in scored_chunks[:top_n]]



if __name__ == "__main__":
# quick manual test
    parrafo = "Hoy estuve tranquilo. Se movio mucho el dia pero la vida va y viene como siempre. Agradezco a Dios y a todos y todas los/las que hoy estan aqui, estuvieron y estaran. Gracias VIDA. El rápido zorro marrón salta sobre el perro perezoso mientras el sol brilla en el cielo azul de la tarde. Este texto sirve para rellenar espacios vacíos en páginas web o documentos cuando aún no tienes la información final lista para mostrar."
    texto_chunkeado = chunk_text(parrafo, chunk_size=100, overlap=20)
    for i, c in enumerate(texto_chunkeado):
        print(f"Chunk {i}: {c}")
    
    embeddings_texto = embed_texts(texto_chunkeado)
    print(f"\n{len(embeddings_texto)} embeddings created")
    print(f"Each embedding has {len(embeddings_texto[0])} dimensions")
    print(f"First embedding preview (first 5 values): {embeddings_texto[0][:5]}")

    result = search("Qué hace este texto?", parrafo, top_n=2)
    print("\nTop matches:")
    for r in result:
        print("-", r)
        
    
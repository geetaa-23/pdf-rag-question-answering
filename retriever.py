import numpy as np

def search(index, query_embedding, k=3):

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        k
    )

    return indices[0]
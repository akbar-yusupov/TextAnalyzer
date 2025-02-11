from src.domain.text_statistics import TextStatistics


def analyze_text(text: str, limit: int = 50) -> list:
    stats = TextStatistics(text)
    tf = stats.compute_tf()
    idf = stats.compute_idf()
    results = []
    for word in tf:
        results.append({
            "word": word,
            "tf": tf[word],
            "idf": idf[word],
        })
    results_sorted = sorted(results, key=lambda x: x["idf"])
    return results_sorted[:limit]

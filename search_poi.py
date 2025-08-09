import sys
from elasticsearch import Elasticsearch

def read_queries(file_path):
    with open(file_path, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main(query_file):
    es = Elasticsearch("http://localhost:9200")
    indices = ["gangwon-poi", "gangwon-poi-fuzzy", "gangwon-poi-ngram"]
    queries = read_queries(query_file)
    
    results = {idx: [] for idx in indices}

    for query in queries:
        for idx in indices:
            res = es.search(
                index=idx,
                body={
                    "query": {
                        "match": {
                            "content_name": {
                                "query": query
                            }
                        }
                    },
                    "_source": ["content_name"],
                    "size": 1
                }
            )
            hits = None
            if hasattr(res, "body"):
                hits = res.body.get("hits", {}).get("hits", [])  # ES 8.x
            else:
                hits = res.get("hits", {}).get("hits", [])
            if hits:
                top_result = hits[0]["_source"]["content_name"]
                score = 1 if query.replace(" ", "") in top_result.replace(" ", "") else 0
            else:
                top_result = None
                score = 0
            results[idx].append({"query": query, "top": top_result, "score": score})

    # 정확도 비교 표 출력
    print("=== 정확도 비교 ===")
    header = f"{'검색어':<20} {'gangwon-poi':<25} {'gangwon-poi-fuzzy':<25} {'gangwon-poi-ngram':<25}"
    print(header)
    for i in range(len(queries)):
        row = [queries[i]]
        for idx in indices:
            val = results[idx][i]["top"] or "-"
            row.append(val)
        print(f"{row[0]:<20} {row[1]:<25} {row[2]:<25} {row[3]:<25}")

    # 각 인덱스별 정확도 점수 출력
    print("\n=== 정확도 점수 ===")
    for idx in indices:
        accuracy = sum(r["score"] for r in results[idx]) / len(queries) * 100
        print(f"{idx}: {accuracy:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python3 search_poi.py [query_file.txt]")
        sys.exit(1)
    query_file = sys.argv[1]
    main(query_file)

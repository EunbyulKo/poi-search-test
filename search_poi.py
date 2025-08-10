import sys
from elasticsearch import Elasticsearch

def read_queries(file_path):
    with open(file_path, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main(query_file):
    es = Elasticsearch("http://localhost:9200")
    indices = ["gangwon-poi", "gangwon-poi-fuzzy", "gangwon-poi-ngram"]
    queries = read_queries(query_file)

    results = {}
    for idx in indices:
        results[idx] = {}
        results[idx][False] = []  # fuzziness 미적용
        results[idx][True] = []   # fuzziness 적용

    for query in queries:
        for idx in indices:
            for fuzz in [False, True]:
                body = {
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
                if fuzz:
                    body["query"]["match"]["content_name"]["fuzziness"] = "AUTO"

                res = es.search(index=idx, body=body)

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
                
                results[idx][fuzz].append({"query": query, "top": top_result, "score": score})

    # 정확도 비교 표 출력
    print("=== 정확도 비교 ===")
    header = f"{'검색어':<20} "
    for idx in indices:
        header += f"{idx + '-fuzzOff':<25} {idx + '-fuzzOn':<25} "
    print(header)

    for i in range(len(queries)):
        row = [queries[i]]
        for idx in indices:
            val_off = results[idx][False][i]["top"] or "-"
            val_on = results[idx][True][i]["top"] or "-"
            row.append(val_off)
            row.append(val_on)
        print(" ".join(f"{v:<25}" for v in row))

    # 각 인덱스별 정확도 점수 출력
    print("\n=== 정확도 점수 ===")
    for idx in indices:
        for fuzz in [False, True]:
            key = "fuzzOn" if fuzz else "fuzzOff"
            accuracy = sum(r["score"] for r in results[idx][fuzz]) / len(queries) * 100
            print(f"{idx}-{key}: {accuracy:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python3 search_poi.py [query_file.txt]")
        sys.exit(1)
    query_file = sys.argv[1]
    main(query_file)

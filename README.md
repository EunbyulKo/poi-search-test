
강원도 관광지 POI 데이터를 Elasticsearch, Logstash를 이용하여 색인하고,  
편집거리 기반 퍼지 검색, Nori 한글 분석기, N-gram 분석기를 적용해 검색 성능을 비교했습니다.

<br/>

---

<br/>

## 📚 사용 기술
- Elasticsearch 8.13.4
- Logstash 8.13.4
- Python 3.13.5

<br/>

## 📦 폴더 및 파일 설명

| 폴더 및 파일 | 설명 |
|--------|------|
| elasticsearch | Elasticsearch 인덱스 설정 정보 |
| logstash | logstash.conf 설정 정보 |
| *-queries.txt | 실험 데이터 |
| search_poi.py | 테스트 실행 파일 |

<br/>

## ⚙️ 테스트 실행

```
python3 search_poi.py default_queries.txt
```

or

```
python search_poi.py default_queries.txt
```



## 1.. Nori 한글 분석기 플러그인 설치

```bash
./bin/elasticsearch-plugin list
./bin/elasticsearch-plugin install analysis-nori
````

> Elasticsearch 기본 분석기는 한국어 형태소 분석에 최적화되어 있지 않아(띄어쓰기만 고려됨) 추가

<br/>
<br/>
<br/>

## 2. 인덱스 매핑 생성

`content_name` 필드에 대해 Nori 분석기와 퍼지 검색을 적용할 새로운 인덱스 `gangwon-poi-fuzzy`를 생성합니다.

```json
PUT /gangwon-poi-fuzzy
{
  "settings": {
    "analysis": {
      "analyzer": {
        "korean_nori": {
          "type": "custom",
          "tokenizer": "nori_tokenizer",
          "filter": [ "lowercase", "nori_readingform", "nori_part_of_speech" ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content_name": {
        "type": "text",
        "analyzer": "korean_nori"
      }
    }
  }
}
```

<br/>
<br/>
<br/>


## 3. 데이터 색인

기존 `gangwon-poi` 인덱스 데이터를 새로 생성한 `gangwon-poi-fuzzy` 인덱스로 복사합니다.

```json
POST _reindex
{
  "source": {
    "index": "gangwon-poi"
  },
  "dest": {
    "index": "gangwon-poi-fuzzy"
  }
}
```

<br/>
<br/>
<br/>


## 4. 데이터 검색 테스트

```json
POST /gangwon-poi-fuzzy/_search
{
  "query": {
    "match": {
      "content_name": {
        "query": "자연"
      }
    }
  }
}
```

이 명령은 `content_name` 필드에서 `"자연"`이라는 단어를 포함하는 문서를 검색합니다.


```json
POST /gangwon-poi-fuzzy/_search
{
  "query": {
    "match": {
      "content_name": {
        "query": "자연",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

퍼지(fuzziness) 옵션을 사용한 `content_name` 필드 검색 예시입니다.
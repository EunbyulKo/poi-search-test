
## 1. 인덱스 매핑 생성

`content_name` 필드에 대해 ngram 분석기를 적용할 새로운 인덱스 
`gangwon-poi-ngram`를 생성합니다.
search_analyzer를 "standard"로 두어 검색 시엔 기본 분석기를 사용하게 합니다.


```json
PUT /gangwon-poi-ngram
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "ngram_tokenizer": {
          "type": "ngram",
          "min_gram": 2,
          "max_gram": 3,
          "token_chars": [ "letter", "digit" ]
        }
      },
      "analyzer": {
        "ngram_analyzer": {
          "type": "custom",
          "tokenizer": "ngram_tokenizer",
          "filter": [ "lowercase" ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content_name": {
        "type": "text",
        "analyzer": "ngram_analyzer",
        "search_analyzer": "standard"
      }
    }
  }
}

```

<br/>
<br/>
<br/>


## 2. 데이터 색인

기존 `gangwon-poi` 인덱스 데이터를 새로 생성한 `gangwon-poi-ngram` 인덱스로 복사합니다.

```json
POST _reindex
{
  "source": {
    "index": "gangwon-poi"
  },
  "dest": {
    "index": "gangwon-poi-ngram"
  }
}
```

<br/>
<br/>
<br/>


## 3. 데이터 검색 테스트

```json
POST /gangwon-poi-ngram/_search
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


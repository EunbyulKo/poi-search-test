## 1. 기본 매핑으로 인덱스 생성

Logstash의 `output { elasticsearch { index => "gangwon-poi" } }` 설정에서  
Elasticsearch에 해당 인덱스가 없으면, 자동으로 기본 매핑(default mapping)이 적용된 인덱스가 생성됩니다.  
따라서 별도로 `curl -X PUT`으로 인덱스를 만들 필요 없이, Logstash를 실행하면 인덱스가 생성되어 있을 것입니다.

<br/>
<br/>

⚠️ 필수아님

Logstash로 데이터를 넣기 전에, 미리 인덱스를 생성할 수도 있습니다.

```bash
curl -X PUT "localhost:9200/gangwon-poi?pretty"
```

⚠️ 주의

자동으로 기본 매핑이 적용되는 것은 편리하지만, 다음과 같이 의도하지 않은 타입 지정이 있을 수 있습니다.

    * 예: "0" (문자열 숫자) → text로 들어감
    * 날짜 포맷 모호할 경우 date로 못 알아봄

그러므로 실무에서는 모든 맵핑을 명시적으로 지정해야 합니다.


<br/>
<br/>
<br/>


## 2. 기본 매핑 확인

```bash
curl -X GET "localhost:9200/gangwon-poi/_mapping?pretty"
```


```json
{
    "gangwon-poi": {
        "mappings": {
            "properties": {
                "accommodation": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "available_facilities": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "category": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "charge": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "closed": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "content_name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "description": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "detail_address": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "details": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "event": {
                    "properties": {
                        "original": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        }
                    }
                },
                "event_period": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "fee": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "homepage": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "id": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "jibun_address": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "log": {
                    "properties": {
                        "file": {
                            "properties": {
                                "path": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "menu": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "nearby_attractions": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "phone": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "price": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "road_address": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "sub_events": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "subcategory": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "tags": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "time": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                }
            }
        }
    }
}
```

여기서 모든 필드가 `text`으로 자동 설정된 것을 확인할 수 있습니다.

<br/>
<br/>

테스트에는 content_name 필드만 사용할 예정입니다.

```json
"content_name": {
  "type": "text",
  "fields": {
    "keyword": {
      "type": "keyword",
      "ignore_above": 256
    }
  }
}
```
* type: text → 형태소 분석을 거쳐 부분 검색 가능 (예: "강릉" 검색 시 "강릉시청" 매치)
* fields.keyword → 분석 없이 원문 전체를 저장하여 정확 일치 검색, 집계, 정렬 가능
* ignore_above: 256 → keyword 필드는 256자 초과 시 색인 안 함

<br/>
<br/>
<br/>


## 3. 데이터 검색 테스트

```bash
curl -X POST "http://localhost:9200/gangwon-poi/_search" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "match": {
        "content_name": "자연"
      }
    }
  }'
```

이 명령은 `content_name` 필드에서 `"자연"`이라는 단어를 포함하는 문서를 검색합니다.

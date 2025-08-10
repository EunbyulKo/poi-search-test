## 📌 데이터 출처
- [한국관광공사_강원도 주요 관광 및 교통 POI 정보](https://www.data.go.kr/data/15032475/fileData.do)  


<br/>
<br/>
<br/>


## 📂 데이터 전처리
원본 데이터는 **EUC-KR** 인코딩이므로, UTF-8로 변환해야 Logstash에서 정상 처리됩니다.

```bash
iconv -c -f euc-kr -t utf-8 "poi-kr-euc-kr.csv" > "poi-kr.csv"

```

> `-c` 옵션은 변환 중 잘못된 문자를 무시합니다.

<br/>
<br/>
<br/>


## ⚙️ Logstash 설정 파일


```conf
input {
  file {
    path => "/your/custom/path/to/data/gangwon/poi-kr.csv"  # ⚠️ 사용자 환경에 맞게 수정
    start_position => "beginning"
    sincedb_path => "/dev/null"  # 매 실행 시 처음부터 읽음 (중복 주의)
  }
}

filter {
  csv {
    separator => ","
    columns => [
      "id", "category", "subcategory", "content-name", "jibun-address", "road-address", "detail-address",
      "phone", "homepage", "time", "price", "fee", "charge", "closed",
      "menu", "nearbyAttractions", "subEvents", "eventPeriod", "accommodation", "availableFacilities",
      "description", "details"
    ]
  }

  ### 🔄 필드명 리네이밍 (하이픈 → 언더스코어)
  mutate {
    rename => { "content-name" => "content_name" }
    rename => { "jibun-address" => "jibun_address" }
    rename => { "road-address" => "road_address" }
    rename => { "detail-address" => "detail_address" }
    rename => { "nearbyAttractions" => "nearby_attractions" }
    rename => { "subEvents" => "sub_events" }
    rename => { "eventPeriod" => "event_period" }
    rename => { "availableFacilities" => "available_facilities" }
  }

  ### 🧹 불필요 필드 제거
  mutate {
    remove_field => ["@timestamp", "@version", "path", "host", "message"]
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "gangwon-poi"
  }
}
```

<br/>
<br/>
<br/>


## ⚠️ 주의사항

1. **인코딩 변환 필수**

   * 원본이 EUC-KR이므로 UTF-8로 변환 후 사용하세요.

2. **경로(`path`) 수정 필수**

   * 로컬 환경에 맞춰서 데이터 경로를 변경해야 합니다.

3. **`start_position => "beginning"` + `sincedb_path => "/dev/null"`**

   * Logstash 실행할 때마다 CSV의 처음부터 데이터를 읽습니다.
   * 같은 인덱스에 여러 번 실행하면 **중복 데이터가 발생**할 수 있습니다.
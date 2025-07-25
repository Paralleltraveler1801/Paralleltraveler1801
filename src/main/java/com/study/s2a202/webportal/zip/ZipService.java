package com.study.s2a202.webportal.zip;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

@Service
public class ZipService {

  @Autowired
  private RestTemplate restTemplate;

  @Autowired
  private ObjectMapper objectMapper;

  public ZipData execute(String zipcode) throws RestClientException, JsonProcessingException {
    // エンドポイント
    String URL = "https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}";

    // APIを呼び出して結果を取得
    String jsonResponse = restTemplate.getForObject(URL, String.class, zipcode);

    // JSONレスポンスをデータオブジェクトに変換
    ZipData zipData = objectMapper.readValue(jsonResponse, ZipData.class);

    return zipData;
  }
}

package com.study.s2a202.webportal.dog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import com.fasterxml.jackson.core.JsonProcessingException;

import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class DogService {

  @Autowired
  private RestTemplate restTemplate;
  @Autowired
  private ObjectMapper objectMapper;

  public DogData execute() throws RestClientException, JsonProcessingException {


    // エンドポイント
    final String URL = "https://dog.ceo/api/breeds/image/random";
    // APIを呼び出して結果を取得
    String jsonResponse = restTemplate.getForObject(URL, String.class);
    // JSONレスポンスをデータオブジェクトに変換
    DogData dogData = objectMapper.readValue(jsonResponse, DogData.class);

    return dogData;
  }
}

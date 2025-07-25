package com.study.s2a202.webportal.dog;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.client.RestClientException;

import com.fasterxml.jackson.core.JsonProcessingException;

import org.springframework.ui.Model;
import org.springframework.beans.factory.annotation.Autowired;

@Controller
public class DogController {

  @Autowired
  private DogService dogService;

  @GetMapping("/dog")
  public String getDog(Model model) {
    // 結果取得
    try {
      DogData data = dogService.execute();
      model.addAttribute("data", data);
      return "dog/result";

    } catch (RestClientException | JsonProcessingException e) {
      model.addAttribute("errorMessage", "検索に失敗しました");
      return "index";
    }
  }

}

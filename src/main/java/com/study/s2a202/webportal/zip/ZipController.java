package com.study.s2a202.webportal.zip;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestClientException;

import com.fasterxml.jackson.core.JsonProcessingException;
import org.springframework.web.bind.annotation.GetMapping;


/**
 * 住所検索コントローラー
 */
@Controller
public class ZipController {

  // 住所検索の業務ロジッククラス
  @Autowired
  private ZipService zipService;

  @GetMapping("/zip")
  public String getZipcode() {
    return "zip/input";
  }

  /**
   * 郵便番号検索を行い、結果を表示するためのリクエストハンドラです。
   * @param zipcode 郵便番号を格納
   * @param model Viewに値を渡すためのオブジェクト
   * @return 郵便番号検索結果を表示する画面のパス
   */
  @PostMapping("/zip")
  public String postZipcode(@RequestParam(name = "zipcode") String zipcode, Model model) {
    try {
      ZipData zipData = zipService.execute(zipcode);
      model.addAttribute("results", zipData);
      return "zip/result";
    } catch (RestClientException | JsonProcessingException e) {
      e.printStackTrace();
      model.addAttribute("errorMessage", "郵便番号検索に失敗しました。");
      return "zip/input";
    }
  }
}

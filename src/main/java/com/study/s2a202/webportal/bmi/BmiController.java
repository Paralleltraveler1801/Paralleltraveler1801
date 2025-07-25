package com.study.s2a202.webportal.bmi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;




@Controller
public class BmiController {

  @Autowired
  private BmiService bmiService;

  @GetMapping("/bmi")
  public String getBmi() {

    return "bmi/input";
  }

  @PostMapping("/bmi")
  public String postBmi(
      Model model,
      @RequestParam(name = "cm") String height,
      @RequestParam(name = "kg") String weight) {
    // 入力チェック
    boolean isValid = bmiService.validate(height, weight);
    if (!isValid) {
      //入力チェックエラーの場合、前画面へ
      return "bmi/input";
    }
    // データを取得
    BmiData data = bmiService.execute(height, weight);
    // データをモデルオブジェクトに設定
    model.addAttribute("bmi", data);

    return "bmi/result";
  }


}

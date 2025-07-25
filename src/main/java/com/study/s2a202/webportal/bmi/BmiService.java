package com.study.s2a202.webportal.bmi;

import org.springframework.stereotype.Service;

@Service
public class BmiService {

  public boolean validate(String height, String weight) {

    // 適正範囲内であるか
    double h, w;
    try {
      h = Double.parseDouble(height);
      w = Double.parseDouble(weight);
    } catch (NumberFormatException e) {
      return false;
    }

    // 身長チェック
    if (h < 30 || h > 250) {
      return false;
    }
    // 体重チェック
    if (w < 5 || w > 200) {
      return false;
    }

    // nullと空文字をみるね～
    if (height == null || height.isEmpty() || weight == null || weight.isEmpty()) {
      return false;
    }

    return true;
  }

  public BmiData execute(String height, String weight) {
    // BMIを格納するクラス生成
    BmiData bmiData = new BmiData();

    // Bmiけいさんするってばよ
    String ans = calc(height, weight);
    bmiData.setAns(ans);
    //コメントするよ
    String comment = judge(ans);
    bmiData.setComment(comment);
    // 画像パスを格納
    String img = img(ans);
    bmiData.setPath(img);

    return bmiData;
  }

  private String judge(String ans) {
    double bmi = Double.parseDouble(ans);
    if (bmi < 16) {
      return "痩せすぎ";
    } else if (bmi < 17.0) {
      return "痩せ";
    } else if (bmi < 18.49) {
      return "痩せぎみ";
    } else if (bmi < 25.0) {
      return "普通体重";
    } else if (bmi < 29.99) {
      return "前肥満";
    } else if (bmi < 34.99) {
      return "肥満（1度）";
    } else if (bmi < 39.99) {
      return "肥満（2度）";
    } else {
      return "肥満（3度）";
    }
  }

  private String img(String ans) {
    double bmi = Double.parseDouble(ans);
    if (bmi < 18.5) {
      return "/img/bmi/gari.png";
    } else if (bmi < 25.0) {
      return "/img/bmi/normal.png";
    } else {
      return "/img/bmi/puni.png";
    }
  }

  private String calc(String height, String weight) {
    // 身長をセンチメートルからメートルへ変換
    double m = Double.parseDouble(height) / 100;
    // BMIを計算
    double bmi = Double.parseDouble(weight) / (m * m);
    // BMiを小数点第三位まで切り捨てて文字列形式で返す
    String ans = String.format("%.3f", bmi);
    return ans;
  }
}

package com.study.s2a202.webportal.practice;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;







@Controller
public class PracticeController {

  @GetMapping("/dojo")
  public String goDojo() {
    return "practice/dojo";
  }
  public String getMethodName(@RequestParam String param) {
      return new String();
  }

  // Level0の処理
  @PostMapping("/level0")
  public String level0() {
    String local = "jouhou";
    String domain = "hcs.ac.jp";

    String e_mail = local + "@" + domain;
    System.out.println(e_mail);

    return "practice/dojo";
  }
// Level1の処理
  @PostMapping("/level1")
  public String level1(Model model) {
    String input = "180 2";

    String[] parts = input.split(" ");
    int x = Integer.parseInt(parts[0]);
    int y = Integer.parseInt(parts[1]);

    int result = (100 + (x * y));

    model.addAttribute("ans", result);
    return "practice/result";
  }
// Level2の処理
  @PostMapping("/level2")
  public String level2(Model model) {
    String input = "namae";
    char result = input.charAt(input.length() - 1);
    model.addAttribute("ans", result);
    return "practice/result";
  }

  // Level3の処理
  @PostMapping("/level3")
  public String level3(@RequestParam(name = "level3")String input, Model model) {
    String ans = input.replaceAll("(?i)[aeiou]", "");

    model.addAttribute("ans", ans);

      return "practice/result";
  }
  // Level4やるよ
  @PostMapping("/level4")
  public String level4(@RequestParam(name = "level4") String input, Model model){
    String[] s = input.split("");

    StringBuilder sb = new StringBuilder();
    for (String c : s) {
      sb.append(c.toLowerCase());
    }
    String line = sb.toString();

    String result = judgeLine(line);

    model.addAttribute("ans", result);
    return "practice/result";
  }

  private String judgeLine(String line) {
    if (line.contains("ooo")) {
      return "o";
    }
    if (line.contains("xxx")) {
      return "x";
    }
    return "draw";
  }


  }

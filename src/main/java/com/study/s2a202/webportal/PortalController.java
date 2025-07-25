package com.study.s2a202.webportal;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import jakarta.servlet.http.HttpSession;




@Controller
public class PortalController {


  @GetMapping("/")
  public String index(HttpSession session) {
  if (session.getAttribute("userId") == null && session.getAttribute("userName") == null) {
    return "redirect:/login"; // 未ログインならloginへ
  }
  return "index";
}
}

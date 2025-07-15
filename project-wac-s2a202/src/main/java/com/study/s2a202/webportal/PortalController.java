package com.study.s2a202.webportal;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class PortalController {

  @GetMapping("/")

  public String index() {
    return "index";
  }
}

package com.study.s2a202.webportal.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.ui.Model;
import jakarta.servlet.http.HttpSession;

@Controller
public class LoginController {

  @GetMapping("/login")
  public String getLogin() {
    return "login"; // login.htmlを返す
  }

  @Autowired
  private LoginService loginService;

  // なんかログイン処理をやらされるみたいですよ
  @PostMapping("/login")
  public String login(
      @RequestParam(name = "userId") String userId,
      @RequestParam(name = "password") String password,
      Model model,
      HttpSession session) {
    // ログインサービスを呼び出してログイン処理を実行
    if (!loginService.login(userId, password)) {
      model.addAttribute("errorMessage", "ユーザーIDまたはパスワードが間違っています。");
      return "login"; // login.htmlを返す
    }
    session.setAttribute("userId", userId);
    // ユーザー名を取得してセッションにセット（LoginServiceにgetUserNameメソッドがある前提）
    String userName = loginService.getUserName(userId);
    session.setAttribute("userName", userName);
    return "redirect:/"; // ログイン成功の場合はリダイレクト
  }

  @GetMapping("/logout")
public String logout(HttpSession session) {
  session.invalidate();
  return "redirect:/login";
}


}

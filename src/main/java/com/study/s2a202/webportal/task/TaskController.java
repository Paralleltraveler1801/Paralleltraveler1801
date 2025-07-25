package com.study.s2a202.webportal.task;




import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.study.s2a202.webportal.user.LoginService;

@Controller
public class TaskController {

  @Autowired
  private LoginService loginService;

  @Autowired
  private TaskService taskService;

  @GetMapping("/task")
  public String getTaskList(Model model) {
    if (!loginService.isLogin()) {
      return "redirect:/login";
    }
    String userId = loginService.getLoginUserId();
    TaskEntity taskEntity = taskService.selectAll(userId);
    model.addAttribute("taskEntity", taskEntity);
    return "task/list";
  }

  // 追加処理
  @PostMapping("/task/insert")
  public String insertTask(
      @RequestParam(name = "title", required = false) String title,
      @RequestParam(name = "limit", required = false) String limit,
      Model model) {

    // 入力チェック
    boolean isValid = taskService.validate(title, limit);
    if (!isValid) {
      model.addAttribute("errorMessage", "入力内容に誤りがあります。");
      return getTaskList(model);
    }

    boolean isSuccess = taskService.insert(loginService.getLoginUserId(), title, limit);
    if (isSuccess) {
      model.addAttribute("message", "正常に登録されました。");
    } else {
      model.addAttribute("errorMessage", "登録できませんでした。");
    }
    return getTaskList(model);
  }

  // 完了処理
  @PostMapping("/task/complete")
  public String completeTask(
      @RequestParam(name = "id", required = false) String id,
      @RequestParam(name = "title", required = false) String title,
      @RequestParam(name = "limit", required = false) String limit,
      Model model) {

    boolean isSuccess = taskService.complete(id);
    if (isSuccess) {
      model.addAttribute("message", "正常に完了しました。");
    } else {
      model.addAttribute("errorMessage", "完了できませんでした。");
    }
    return getTaskList(model);
  }

  // 削除処理
  @PostMapping("/task/delete")
  public String deleteTask(
      @RequestParam(name = "id", required = false) String id,
      @RequestParam(name = "title", required = false) String title,
      @RequestParam(name = "limit", required = false) String limit,
      Model model) {

    boolean isSuccess = taskService.delete(id);
    if (isSuccess) {
      model.addAttribute("message", "正常に削除されました。");
    } else {
      model.addAttribute("errorMessage", "削除できませんでした。");
    }
    return getTaskList(model);
  }


}

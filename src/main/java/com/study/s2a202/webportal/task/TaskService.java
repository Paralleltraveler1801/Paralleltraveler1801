package com.study.s2a202.webportal.task;



import java.text.SimpleDateFormat;
import java.util.Date;
import java.text.ParseException;
import java.sql.SQLException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.study.s2a202.webportal.task.TaskService;



@Service
public class TaskService {
  @Autowired
  private TaskRepository taskRepository;


  public TaskEntity selectAll(String userId) {
    // // ダミーデータを設定
    // TaskData taskData = new TaskData(
    // 1,
    // userId,
    // "ダミータスク1",
    // Date.valueOf("1111-11-11"),
    // false);
    // TaskEntity taskEntity = new TaskEntity();
    // taskEntity.getTaskList().add(taskData);

    // DBからデータを取得
    TaskEntity taskEntity = taskRepository.findAll(userId);
    return taskEntity;
    // return taskEntity;

  }

  public boolean insert(String userId, String title, String limit) {
    Date limitdayDate = null;
    try {
      SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
      limitdayDate = new Date(format.parse(limit).getTime());
    } catch (ParseException e) {
      e.printStackTrace();
    }
    TaskData taskData = new TaskData(0, userId, title, limitdayDate, false, 1);
    try {
      taskRepository.save(taskData);
    } catch (SQLException e) {
      e.printStackTrace();
      return false;
    }
    return true;
  }

  boolean validate(String comment, String limitday){
    if (comment == null || comment.isBlank() || comment.length() > 50) {
      return false;

    }
    if (limitday == null || limitday.isBlank()) {
      return false;
    }
    try {
      SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
      format.parse(limitday);
    } catch (ParseException e) {
      return false;
    }
    return true;
  }



  // 完了処理
  public boolean complete(String id) {
    int i = Integer.parseInt(id);
    try {
      taskRepository.update(i);
    } catch (SQLException e) {
      e.printStackTrace();
      return false;
    }
    return true;
  }

  // 削除処理
  public boolean delete(String id) {
    int i = Integer.parseInt(id);
    try {
      taskRepository.delete(i);
    } catch (SQLException e) {
      e.printStackTrace();
      return false;
    }
    return true;
  }


}

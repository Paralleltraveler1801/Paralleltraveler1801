package com.study.s2a202.webportal.task;

import java.util.ArrayList;
import java.util.List;

public record TaskEntity(
  List<TaskData> taskList,
  String errorMessage){

  public TaskEntity() {
    this(new ArrayList<>(),"");
  }
}

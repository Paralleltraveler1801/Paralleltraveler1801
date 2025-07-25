package com.study.s2a202.webportal.task;
import java.util.Date;

public record TaskData(
// タスクID：主キー、SQLにて自動採番
  int id,
  // ユーザーID（メールアドレス）:Userテーブルの主キーと紐づく
  String userId,
  //件名：必須入力
  String title,
  //期限日：必須入力
    Date limitday,


  // 完了フラグ：デフォはfalse、完了時はtrue
  boolean isComplete,

  // 優先度：必須入力
  int priority
){


}

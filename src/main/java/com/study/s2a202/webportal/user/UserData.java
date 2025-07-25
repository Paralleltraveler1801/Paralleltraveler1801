package com.study.s2a202.webportal.user;

public record UserData(
// ゆーざーID
  String userId,
  // パスワード
  String password,
  // ユーザーネーム：必須入力
  String userName,
  // 権限：管理
  String role,
  // アカウントの有効性
  boolean enabled
) {
  
}

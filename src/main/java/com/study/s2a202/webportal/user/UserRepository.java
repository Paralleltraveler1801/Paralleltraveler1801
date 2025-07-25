package com.study.s2a202.webportal.user;

import java.util.HashMap;
import java.util.Map;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class UserRepository {
  @Autowired
  private NamedParameterJdbcTemplate jdbc;

  public UserData login(String userId, String password) {
    // SQLのログインチェック
    final String SQL_LOGIN = "SELECT user_name, role, enabled FROM user_m WHERE user_id = :userId AND password = :password AND enabled = true";

    // パラメータを格納するためのマップを生成
    Map<String, Object> params = new HashMap<>();
    params.put("userId", userId);
    params.put("password", password);

    // データベースのクエリを実行し、結果を取得
    List<Map<String, Object>> resultList = jdbc.queryForList(SQL_LOGIN, params);

    UserData userData = null;
    if (resultList.size() == 1) {
      Map<String, Object> result = resultList.get(0);
      String userName = (String) result.get("user_name");
      String role = (String) result.get("role");
      boolean enabled = (Boolean) result.get("enabled");
      userData = new UserData(userId, "****", userName, role, enabled);
    }
    return userData;
  }
}

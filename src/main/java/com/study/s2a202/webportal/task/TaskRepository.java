package com.study.s2a202.webportal.task;

import java.sql.Date;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;

/**
 * タスク管理に関わるDBアクセスを実現するクラスです。
 * 処理が継続できない場合は呼び出し元へ例外をスローします。
 *
 * @author ABB
 */
@Repository
public class TaskRepository {

  @Autowired
  private NamedParameterJdbcTemplate jdbc;

  /**
   * 指定されたユーザーIDに関連するタスク情報を検索します。
   *
   * @param userId ユーザーID
   * @return 指定されたユーザーIDに関連するタスク情報のリスト
   */
  public TaskEntity findAll(String userId) {
    final String SQL_SELECT_ALL = "SELECT id, title, limitday, complete FROM task_t WHERE user_id = :userId ORDER BY limitday";
    Map<String, Object> params = new HashMap<>();
    params.put("userId", userId);
    List<Map<String, Object>> resultList = jdbc.queryForList(SQL_SELECT_ALL, params);

    List<TaskData> tasks = new ArrayList<>();
    for (Map<String, Object> map : resultList) {
        int id = (Integer) map.get("id");
        String title = (String) map.get("title");
        Date limitday = (Date) map.get("limitday");
        boolean complete = (Boolean) map.get("complete");
        TaskData data = new TaskData(id, userId, title, limitday, complete, 1); // 優先度はデフォルトで1としています
        tasks.add(data);
    }
    return new TaskEntity(tasks, "");
  }

  /**
   * タスク情報を1件登録します。
   *
   * @param taskData 保存するタスクデータ
   * @return 更新された行数
   * @throws SQLException 更新に失敗した場合にスローされる例外
   */
  public int save(TaskData taskData) throws SQLException {
    final String SQL_INSERT_ONE = "INSERT INTO task_t(id, user_id, title, limitday, complete) " +
        "VALUES ((SELECT COALESCE(MAX(id), 0) + 1 FROM task_t), :userId, :title, :limitday, false)";
    Map<String, Object> params = new HashMap<>();
    params.put("userId", taskData.userId());
    params.put("title", taskData.title());
    params.put("limitday", taskData.limitday());

    int updateRow = jdbc.update(SQL_INSERT_ONE, params);
    if (updateRow != 1) {
      throw new SQLException("登録件数異常: " + updateRow);
    }
    return updateRow;
  }

  /**
   * タスク情報を1件削除します。
   *
   * @param id 削除するデータのID
   * @return 更新された行数
   * @throws SQLException 更新に失敗した場合にスローされる例外
   */
  public int delete(int id) throws SQLException {
    final String SQL_DELETE_ONE = "DELETE FROM task_t WHERE id = :id";
    Map<String, Object> params = new HashMap<>();
    params.put("id", id);

    int updateRow = jdbc.update(SQL_DELETE_ONE, params);
    if (updateRow != 1) {
      throw new SQLException("削除件数異常: " + updateRow);
    }
    return updateRow;
  }

  /**
   * タスク情報を1件更新します（完了フラグをtrueに）。
   *
   * @param id 更新するデータのID
   * @return 更新された行数
   * @throws SQLException 更新に失敗した場合にスローされる例外
   */
  public int update(int id) throws SQLException {
    final String SQL_UPDATE_ONE = "UPDATE task_t SET complete = true WHERE id = :id";
    Map<String, Object> params = new HashMap<>();
    params.put("id", id);

    int updateRow = jdbc.update(SQL_UPDATE_ONE, params);
    if (updateRow != 1) {
      throw new SQLException("更新件数異常: " + updateRow);
    }
    return updateRow;
  }

  


}

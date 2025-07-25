package com.study.s2a202.webportal.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import jakarta.servlet.http.HttpSession;

/**
 * ログインサービスクラスです。
 * ログイン関連の操作を提供します。
 */
@Transactional
@Service
public class LoginService {

  /** セッションオブジェクト */
  @Autowired
  private HttpSession session;

  /** ユーザーリポジトリ */
  @Autowired
  private UserRepository userRepository;

  /** セッションキー（ログインユーザー情報） */
  private static final String SESSION_USER_DATA_KEY = "userData";

  /**
   * ログイン処理（true/false返すシンプルなやつ）
   */
  public boolean login(String userId, String password) {
    UserData userData = userRepository.login(userId, password);
    if (userData == null) {
      return false;
    }
    session.setAttribute(SESSION_USER_DATA_KEY, userData);
    return true;
  }

  /**
   * ログイン処理（ユーザー情報を返すバージョン）
   */
  public UserData doLogin(String userId, String password) {
    UserData userData = userRepository.login(userId, password);
    if (userData != null) {
      session.setAttribute(SESSION_USER_DATA_KEY, userData);
    }
    return userData;
  }

  /**
   * ログアウト処理
   */
  public void logout() {
    session.invalidate();
  }

  /**
   * ログイン中ユーザーのユーザーIDを取得します。
   *
   * @return ログイン中ユーザーのユーザーID（ログインしていない場合は "Unknown User"）
   */
  public String getLoginUserId() {
    UserData userData = (UserData) session.getAttribute(SESSION_USER_DATA_KEY);
    if (userData == null) {
      return "Unknown User";
    }
    return userData.userId();
  }

  /**
   * ログインしているかどうかを判定します。
   *
   * @return true: ログイン中 / false: ログインしていない
   */
  public boolean isLogin() {
    return session.getAttribute(SESSION_USER_DATA_KEY) != null;
  }

  /**
   * ログインしているユーザーのユーザー名を取得します。
   * @return ユーザー名（未ログイン時は "Unknown User"）
   */
  public String getUserName(String userId) {
    UserData userData = (UserData) session.getAttribute(SESSION_USER_DATA_KEY);
    if (userData == null) {
      return "Unknown User";
    }
    // UserDataにgetUserName()またはuserName()がある前提
    return userData.userName();
  }
}

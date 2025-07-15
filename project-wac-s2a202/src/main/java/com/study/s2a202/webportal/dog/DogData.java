package com.study.s2a202.webportal.dog;

public record DogData (
  // Canis lupus familiaris　の画像のURL
  String message,

  // APIの結果ステータス
  String status,

  // 処理失敗時のエラーメッセージ
  String errorMessage) {


  // エラーメッセージの設定
  public DogData withErrorMessage(String newErrorMessage) {
    return new DogData(this.message, this.status, newErrorMessage);
  }

}

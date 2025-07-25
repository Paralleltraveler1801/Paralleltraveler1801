package com.study.s2a202.webportal.zip;

import java.util.List;

public record ZipData(
    // ステータス
    String status,
    // メッセージ
    String message,
    // 郵便番号のリスト
    List<Results> results,
    // エラーメッセージ
    String errorMessage) {
  public record Results(
      // 郵便番号
      String zipcode,
      // 都道府県コード
      String prefcode,
      // 都道府県
      String address1,
      // 市区町村名
      String address2,
      // 町域名
      String address3,
      // 都道府県カナ
      String kana1,
      // 市区町村名カナ
      String kana2,
      // 町域名カナ
      String kana3) {
  }
}

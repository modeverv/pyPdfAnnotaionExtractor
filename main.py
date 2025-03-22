import fitz
import sys
import argparse

def extract_highlights(pdf_path):
    """
    PDFファイルからハイライトされたテキストを抽出する関数

    Args:
        pdf_path (str): PDFファイルのパス
        output_file (str, optional): 出力ファイルのパス。指定しない場合は標準出力に表示

    Returns:
        list: ハイライトされたテキストのリスト
    """
    try:
        # PDFファイルを開く
        doc = fitz.open(pdf_path)
        highlights = []

        # 各ページを処理
        for page_num, page in enumerate(doc, 1):
            # ページ内のアノテーションを処理
            for annot in page.annots():
                # タイプ8はハイライト
                if annot.type[0] == 8:
                    # ハイライト部分のテキストを取得
                    highlighted_text = page.get_textbox(annot.rect)
                    if highlighted_text.strip():  # 空白でない場合のみ追加
                        highlights.append({
                            'page': page_num,
                            'text': highlighted_text.strip()
                        })

        for highlight in highlights:
            print(f"ページ {highlight['page']}:")
            print(f"{highlight['text']}\n")

        return highlights

    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        return []

def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='PDFファイルからハイライトされたテキストを抽出します')
    parser.add_argument('pdf_path', help='PDFファイルのパス')
    args = parser.parse_args()
    # ハイライト抽出実行
    extract_highlights(args.pdf_path)

if __name__ == "__main__":
    main()
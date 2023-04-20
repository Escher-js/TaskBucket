import json

def json_to_html(json_file, html_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>JSON to HTML Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>名前</th>
                <th>詳細</th>
                <th>緊急度</th>
                <th>重要度</th>
                <th>親</th>
            </tr>
        </thead>
        <tbody>
'''

    for item in data:
        html += f'''<tr>
            <td>{item["name"]}</td>
            <td>{item["detail"]}</td>
            <td>{item["urgency"]}</td>
            <td>{item["importance"]}</td>
            <td>{item["parent"] if item["parent"] else "null"}</td>
        </tr>
'''

    html += '''        </tbody>
    </table>
</body>
</html>
'''

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# JSONファイルとHTMLファイルのパスを指定して、json_to_html関数を呼び出します。
json_file = 'tasks.json'
html_file = 'tasks.html'
json_to_html(json_file, html_file)

import json

def json_to_html(json_file, html_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tasks = [[[] for _ in range(5)] for _ in range(5)]

    for item in data:
        urgency_idx = item["urgency"] - 1
        importance_idx = item["importance"] - 1
        tasks[urgency_idx][importance_idx].append(item["name"])

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
                <th></th>
'''

    for i in range(1, 6):
        html += f'<th>重要度 {i}</th>'
    html += '</tr></thead><tbody>'

    for i in range(5):
        html += f'<tr><th>緊急度 {i + 1}</th>'
        for j in range(5):
            html += f'<td>{", ".join(tasks[i][j])}</td>'
        html += '</tr>'

    html += '''    </tbody>
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

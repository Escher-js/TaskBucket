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
        body {
            font-family: Arial, sans-serif;
            background-color: #222831;
            color: #eeeeee;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            table-layout: fixed;
        }
        th, td {
            border: none;
            padding: 8px;
            text-align: left;
            font-size: 14px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        th {
            background-color: #393e46;
            padding: 12px;
        }
        td {
            background-color: #30475e;
            max-width: 150px;
            white-space: pre-wrap; /* 改行を有効にする */
            word-wrap: break-word; /* 単語がセルの幅を超えた場合に改行する */
        }
        tbody tr {
    height: 20%; /* 各行の高さを均等にする */
}
.item {
    display: inline-block;
    border: 1px solid #eeeeee;
    border-radius: 5px;
    padding: 2px 5px;
    margin: 2px;
}

    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th></th>
'''

    for i in range(5):
        html += f'<tr><th>緊急度 {i + 1}</th>'
        for j in range(5):
            task_list = tasks[i][j]
            task_items = ['<span class="item">' + task + '</span>' for task in task_list]
            task_html = "<br>".join(task_items)
            html += f'<td>{task_html}</td>'
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

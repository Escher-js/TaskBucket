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
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            tbody tr {
                height: 20%;
            }
            .item {
                display: inline-block;
                border: 1px solid #eeeeee;
                border-radius: 5px;
                padding: 2px 5px;
                margin: 2px;
                cursor: grab;
            }
        </style>
        <script>
            function allowDrop(ev) {
                ev.preventDefault();
            }

            function drag(ev) {
                ev.dataTransfer.setData("text", ev.target.id);
            }

            function drop(ev) {
                ev.preventDefault();
                var data = ev.dataTransfer.getData("text");
                ev.target.appendChild(document.getElementById(data));
            }
        </script>
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
            task_list = tasks[i][j]
            task_items = ['<span class="item" id="item{idx}" draggable="true" ondragstart="drag(event)">{task}</span>'.format(idx=idx, task=task) for idx, task in enumerate(task_list, start=1)]
            task_html = "<br>".join(task_items)
            html += f'<td ondrop="drop(event)" ondragover="allowDrop(event)">{task_html}</td>'
        html += '</tr>'

    html += '''
        </tbody>
        </table>
        </body>
        </html>
    '''
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# JSONファイルと出力するHTMLファイルの名前を指定して関数を実行
json_file = 'input.json' # 入力するJSONファイル名
html_file = 'output.html' # 出力するHTMLファイル名
json_to_html(json_file, html_file)


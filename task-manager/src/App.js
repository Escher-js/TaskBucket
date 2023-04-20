import React from 'react';
import TaskTable from './components/TaskTable';
import { jsonToTasks } from './utils/jsonToTasks';
import './App.css';

// 与えられたJSONデータ
const jsonData = [
  // JSONデータをここに配置する
];

// JSONデータを2次元配列に変換する
const tasks = jsonToTasks(jsonData);

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Task Manager</h1>
      </header>
      <main className="App-main">
        <TaskTable tasks={tasks} />
      </main>
    </div>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import TaskTable from './components/TaskTable';
import CreateTask from './components/CreateTask';
import { jsonToTasks } from './utils/jsonToTasks';
import jsonData from './data/tasks.json';
import './App.css';

const initialTasks = JSON.parse(localStorage.getItem('tasks')) || jsonToTasks(jsonData);


function App() {
  const [tasks, setTasks] = useState(initialTasks);

  const handleCreateTask = (newTask) => {
    const updatedTasks = [...tasks];
    const i = 5 - newTask.importance;
    const j = newTask.urgency - 1;
    updatedTasks[i][j].push(newTask.name);
    setTasks(updatedTasks);
  };

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Task Manager</h1>
      </header>
      <main className="App-main">
        <CreateTask onSubmit={handleCreateTask} />
        <TaskTable tasks={tasks} />
      </main>
    </div>
  );
}

export default App;

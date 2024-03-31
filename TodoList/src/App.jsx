import { useEffect, useState } from 'react';
import NavBar from './components/NavBar';
import {FaEdit} from "react-icons/fa";
import {AiFillDelete} from "react-icons/ai";
import { v4 as uuidv4 } from 'uuid';

function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);
  const [showFinished, setShowFinished] = useState(true);

  useEffect(() => {
    const todosFromLocalStorage = JSON.parse(localStorage.getItem("todos"));
    if (todosFromLocalStorage) {
      setTodos(todosFromLocalStorage);
    }
  }, []);

  const saveToLS = () => {
    localStorage.setItem("todos", JSON.stringify(todos));
  };

  const toggleFinished = () => {
    setShowFinished(prevState => !prevState);
  };

  const handleEdit = (e, id) => {
    const todoToEdit = todos.find(item => item.id === id);
    if (todoToEdit) {
      setTodo(todoToEdit.todo);
      const newTodos = todos.filter(item => item.id !== id);
      setTodos(newTodos);
      saveToLS();
    }
  };  

  const handleDelete = (id) => {
    const isConfirmed = window.confirm("Are you sure you want to delete this todo?");
    if (isConfirmed) {
      const newTodos = todos.filter(item => item.id !== id);
      setTodos(newTodos);
      saveToLS();
    }
  };

  const handleAdd = () => {
    setTodos([...todos, { id: uuidv4(), todo, isCompleted: false }]);
    setTodo("");
    saveToLS();
  };

  const handleChange = (e) => {
    setTodo(e.target.value);
  };

  const handleCheckbox = (e) => {
    const id = e.target.name;
    const index = todos.findIndex(item => item.id === id);
    let newTodos = [...todos]; // Copy the todos array
    newTodos[index].isCompleted = !newTodos[index].isCompleted;
    setTodos(newTodos);
    saveToLS();
  };

  return (
    <> 
      <NavBar />
      <div className="container mx-auto my-5 rounded-xl p-5 bg-violet-100 min-h-[80vh] w-1/2">
        <h1 className='text-center text-xl font-bold mb-4'>Manage Your Todos At One Place</h1>
        <div className="addTodo flex items-center gap-4 mb-4">
          <input name="todo" onChange={handleChange} value={todo} type="text" className='flex-1 px-5 py-1 border border-gray-300 rounded-full'/>
          <button onClick={handleAdd} disabled={!todo.trim()} className='w-20 bg-violet-800 hover:bg-violet-950 px-4 py-2 text-sm font-bold text-white rounded-md disabled:bg-violet-300'>Save</button>
        </div>
        <input className='my-4' onClick={toggleFinished} type="checkbox" checked={showFinished} /> Show Finished
        <h2 className='text-lg font-bold mb-2 mt-4'>Your Todos</h2>
        <div className="todos">
          {todos.length === 0 && <div>No Todos to display</div>}
          {todos.map(item => (
            (showFinished || !item.isCompleted) && <div className="todo flex items-center justify-between border-b border-gray-300 py-2" key={item.id}>
              <input onChange={handleCheckbox} type="checkbox" checked={item.isCompleted} name={item.id} id={item.id} className="mr-2"/>
              <div className={`task-text flex-1 ${item.isCompleted ? "line-through" : ""}`} style={{ wordBreak: 'break-word' }}>{item.todo}</div>
              <div className="buttons">
                <button onClick={(e)=>{handleEdit(e, item.id)}} className='bg-violet-800 hover:bg-violet-950 px-2 py-1 text-sm font-bold text-white rounded-md mr-2'><FaEdit/></button>
                <button onClick={() => handleDelete(item.id)} className='bg-violet-800 hover:bg-violet-950 px-2 py-1 text-sm font-bold text-white rounded-md'><AiFillDelete/></button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default App;

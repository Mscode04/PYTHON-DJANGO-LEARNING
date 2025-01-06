
import './App.css';
import Create_Image from './Components/Create_Image';
import Curd from './Components/Curd';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
function App() {
  return (
    <div className="App">
      <h1>hello</h1>
      <ToastContainer />
      {/* <Curd/> */}
      <Create_Image></Create_Image>
    </div>
  );
}

export default App;

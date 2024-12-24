import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/Register";
import Dealers from "./components/Dealers/Dealers";
import Dealer from "./components/Dealers/Dealer";
import PostReview from "./components/Dealers/PostReview";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />

      {/* New register route*/}
      <Route path="/register" element={<Register />} />

      {/* New dealers route*/}
      <Route path="/dealers" element={<Dealers />} />

      {/* New dealer route*/}
      <Route path="/dealer/:id" element={<Dealer />} />

      {/* New post review route*/}
      <Route path="/postreview/:id" element={<PostReview />} />
    </Routes>
  );
}
// export App component as default module so that it is available to other modules
export default App;

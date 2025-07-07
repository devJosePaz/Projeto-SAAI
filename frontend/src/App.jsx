// SAAI/frontend/src/App.jsx
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import StudyPlanForm from "./pages/StudyPlanForm";

function App() {
  return (
    <Router>
      <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
        <h1 style={{ textAlign: "center", color: "#333" }}>Sistema SAAI</h1>

        <nav style={{ marginBottom: "20px", textAlign: "center" }}>
          <Link
            to="/register"
            style={{
              marginRight: "15px",
              textDecoration: "none",
              color: "#007bff",
              fontWeight: "bold",
            }}
          >
            Cadastrar
          </Link>
          <Link
            to="/login"
            style={{
              marginRight: "15px", // Adicionado para espaçar do próximo link
              textDecoration: "none",
              color: "#007bff",
              fontWeight: "bold",
            }}
          >
            Login
          </Link>
          {/* NOVO LINK: Para a página de Gerar Plano de Estudo */}
          <Link
            to="/generate-plan"
            style={{
              textDecoration: "none",
              color: "#28a745", // Cor diferente para destacar
              fontWeight: "bold",
            }}
          >
            Gerar Plano de Estudo
          </Link>
        </nav>

        <hr style={{ borderTop: "1px solid #eee", marginBottom: "20px" }} />

        <Routes>
          {/* Rota para a página de registro */}
          <Route path="/register" element={<Register />} />

          {/* Rota para a página de login */}
          <Route path="/login" element={<Login />} />

          {/* Rota padrão para a raiz (/) */}
          <Route
            path="/"
            element={
              <div
                style={{
                  textAlign: "center",
                  padding: "50px",
                  background: "#f9f9f9",
                  borderRadius: "8px",
                }}
              >
                <h2>Bem-vindo ao SAAI!</h2>
                <p>
                  Por favor, use os links acima para Cadastrar ou fazer Login.
                </p>
              </div>
            }
          />

          {/* Rota para a página de Gerar Plano de Estudo */}
          <Route path="/generate-plan" element={<StudyPlanForm />} />

          {/* Rota 404 (Not Found) - Removida a duplicação */}
          <Route
            path="*"
            element={
              <div
                style={{
                  textAlign: "center",
                  padding: "50px",
                  background: "#f9f9f9",
                  borderRadius: "8px",
                  color: "red",
                }}
              >
                <h2>404 - Página Não Encontrada</h2>
                <p>A URL que você tentou acessar não existe.</p>
              </div>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

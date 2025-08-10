// SAAI/frontend/src/pages/Login.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom"; // Importar useNavigate

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [mensagem, setMensagem] = useState("");
  const [token, setToken] = useState(""); // Ainda vamos exibir por enquanto
  const navigate = useNavigate(); // Hook para navegação programática

  const handleLogin = async () => {
    try {
      const resposta = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        setMensagem("Login bem-sucedido!");
        setToken(dados.access_token);
        // PASSO NOVO E CRÍTICO: Salvar o token no localStorage
        localStorage.setItem("jwt_token", dados.access_token);
        // Opcional: Limpar campos
        setEmail("");
        setPassword("");
        // CRÍTICO: Redirecionar para a rota protegida
        navigate("/generate-plan");
      } else {
        setMensagem(`Erro: ${dados.detail}`);
        setToken("");
      }
    } catch (err) {
      setMensagem("Erro na conexão com o servidor");
      setToken("");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Login de Usuário</h2>
      <input
        type="text"
        placeholder="Usuário"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br />
      <button onClick={handleLogin}>Entrar</button>
      <p>{mensagem}</p>
      {token && ( // Manter a exibição do token por enquanto para debug
        <div>
          <p>
            <strong>Token JWT:</strong>
          </p>
          <textarea
            readOnly
            value={token}
            style={{ width: "100%", height: "100px" }}
          />
        </div>
      )}
    </div>
  );
}

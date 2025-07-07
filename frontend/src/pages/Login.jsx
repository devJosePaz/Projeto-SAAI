import { useState } from "react";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [mensagem, setMensagem] = useState("");
  const [token, setToken] = useState("");

  const handleLogin = async () => {
    try {
      const resposta = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        setMensagem("Login bem-sucedido!");
        setToken(dados.access_token);
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
        value={username}
        onChange={(e) => setUsername(e.target.value)}
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
      {token && (
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

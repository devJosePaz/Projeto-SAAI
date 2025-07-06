import { useState } from "react";

export default function CadastroUsuario() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [mensagem, setMensagem] = useState("");

  const handleCadastro = async () => {
    try {
      const resposta = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (resposta.ok) {
        setMensagem("Usuário cadastrado com sucesso!");
        setUsername("");
        setPassword("");
      } else {
        const erro = await resposta.json();
        setMensagem(`Erro: ${erro.detail}`);
      }
    } catch (err) {
      setMensagem("Erro na conexão com o servidor");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Cadastro de Usuário</h2>
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
      <button onClick={handleCadastro}>Cadastrar</button>
      <p>{mensagem}</p>
    </div>
  );
}

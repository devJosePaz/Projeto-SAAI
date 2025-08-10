// SAAI/frontend/src/pages/Register.jsx
import { useState } from "react";

export default function Register() {
  // Nome do componente ajustado
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [mensagem, setMensagem] = useState("");

  const handleCadastro = async () => {
    try {
      const resposta = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({email, password }), // <--- ESTA LINHA É CRÍTICA
      });

      if (resposta.ok) {
        setMensagem("Usuário cadastrado com sucesso!");
        setEmail("");
        setPassword("");
      } else {
        const erro = await resposta.json();
        // Adicione um console.error para ver os detalhes do erro 422
        console.error("Erro no cadastro (detalhes):", erro);
        setMensagem(`Erro: ${erro.detail || "Ocorreu um erro."}`); // Melhorar a mensagem de erro
      }
    } catch (err) {
      console.error("Erro na conexão com o servidor:", err); // Log de erro de rede
      setMensagem("Erro na conexão com o servidor");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Cadastro de Usuário</h2>
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
      <button onClick={handleCadastro}>Cadastrar</button>
      <p>{mensagem}</p>
    </div>
  );
}

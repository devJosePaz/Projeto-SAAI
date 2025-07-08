import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function StudyPlanForm() {
  const [theme, setTheme] = useState("");
  const [dailyTime, setDailyTime] = useState(""); // Estado no frontend (camelCase)
  const [objective, setObjective] = useState("");
  const [learningStyle, setLearningStyle] = useState("visual");
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("jwt_token");
    if (!token) {
      alert("Você precisa estar logado para acessar esta página.");
      navigate("/login");
    } else {
      setLoading(false);
    }
  }, [navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const token = localStorage.getItem("jwt_token");
    if (!token) {
      setErrorMessage("Erro: Você não está logado.");
      return;
    }

    const formData = {
      // CORREÇÃO AQUI: Mapear nomes do frontend (camelCase) para backend (snake_case)
      theme: theme,
      daily_time: parseInt(dailyTime), // 'daily_time' para corresponder ao backend
      objective: objective,
      learning_style: learningStyle,
    };

    console.log("Dados do formulário a serem enviados:", formData);
    setErrorMessage("");

    try {
      const response = await fetch("http://localhost:8000/study_plans/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        alert("Plano de estudo gerado com sucesso!");
        console.log("Plano gerado:", data);
        setTheme("");
        setDailyTime("");
        setObjective("");
        setLearningStyle("visual");
      } else {
        const errorData = await response.json();
        // O FastAPI geralmente retorna detalhes do erro 422 aqui
        console.error("Erro ao gerar plano (detalhes):", errorData);
        setErrorMessage(
          `Erro ao gerar plano: ${errorData.detail || "Ocorreu um erro."}`
        );
        if (response.status === 401) {
          localStorage.removeItem("jwt_token");
          navigate("/login");
        }
      }
    } catch (error) {
      console.error("Erro na submissão do formulário:", error);
      setErrorMessage("Erro na conexão com o servidor.");
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: "center", padding: "50px" }}>Carregando...</div>
    );
  }

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "40px auto",
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "8px",
        boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
      }}
    >
      <h2 style={{ textAlign: "center", marginBottom: "30px", color: "#333" }}>
        Gerar Plano de Estudo
      </h2>

      {errorMessage && (
        <p style={{ color: "red", textAlign: "center" }}>{errorMessage}</p>
      )}

      <form
        onSubmit={handleSubmit}
        style={{ display: "flex", flexDirection: "column", gap: "15px" }}
      >
        <div>
          <label
            htmlFor="theme"
            style={{
              display: "block",
              marginBottom: "5px",
              fontWeight: "bold",
            }}
          >
            Tema de Estudo:
          </label>
          <input
            type="text"
            id="theme"
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
            placeholder="Ex: Introdução à Inteligência Artificial"
            required
            style={{
              width: "100%",
              padding: "10px",
              border: "1px solid #ccc",
              borderRadius: "4px",
              boxSizing: "border-box",
            }}
          />
        </div>

        <div>
          <label
            htmlFor="dailyTime"
            style={{
              display: "block",
              marginBottom: "5px",
              fontWeight: "bold",
            }}
          >
            Tempo Diário de Estudo (minutos):
          </label>
          <input
            type="number"
            id="dailyTime"
            value={dailyTime}
            onChange={(e) => setDailyTime(e.target.value)}
            placeholder="Ex: 60 (para 1 hora)"
            min="10"
            required
            style={{
              width: "100%",
              padding: "10px",
              border: "1px solid #ccc",
              borderRadius: "4px",
              boxSizing: "border-box",
            }}
          />
        </div>

        <div>
          <label
            htmlFor="objective"
            style={{
              display: "block",
              marginBottom: "5px",
              fontWeight: "bold",
            }}
          >
            Objetivo com o Estudo:
          </label>
          <textarea
            id="objective"
            value={objective}
            onChange={(e) => setObjective(e.target.value)}
            placeholder="Ex: Entender os fundamentos de ML para criar um modelo simples."
            rows="4"
            required
            style={{
              width: "100%",
              padding: "10px",
              border: "1px solid #ccc",
              borderRadius: "4px",
              boxSizing: "border-box",
              resize: "vertical",
            }}
          />
        </div>

        <div>
          <label
            htmlFor="learningStyle"
            style={{
              display: "block",
              marginBottom: "5px",
              fontWeight: "bold",
            }}
          >
            Estilo de Aprendizagem:
          </label>
          <select
            id="learningStyle"
            value={learningStyle}
            onChange={(e) => setLearningStyle(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              border: "1px solid #ccc",
              borderRadius: "4px",
              boxSizing: "border-box",
            }}
          >
            <option value="visual">Visual (aprende melhor vendo)</option>
            <option value="auditory">Auditivo (aprende melhor ouvindo)</option>
            <option value="reading_writing">
              Leitura/Escrita (aprende melhor lendo e escrevendo)
            </option>
            <option value="kinesthetic">
              Cinestésico (aprende melhor fazendo/praticando)
            </option>
          </select>
        </div>

        <button
          type="submit"
          style={{
            padding: "12px 20px",
            backgroundColor: "#28a745",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
            fontSize: "16px",
            marginTop: "20px",
          }}
        >
          Gerar Plano de Estudo
        </button>
      </form>
    </div>
  );
}

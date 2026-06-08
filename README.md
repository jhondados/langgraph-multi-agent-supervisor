# 🎯 LangGraph Multi-Agent Supervisor

[![LangGraph](https://img.shields.io/badge/LangGraph-0.2-orange)](.) [![Agents](https://img.shields.io/badge/Agents-6%20specialized-blue)](.) [![Production](https://img.shields.io/badge/Status-Production-green)](.)

> **Production supervisor architecture** with LangGraph. Orchestrator routes tasks to specialized agents: Researcher, Coder, Data Analyst, Writer, SQL Expert, Web Scraper. Shared memory across all agents.

## 🤖 Agent Network
```
User Task
    └─▶ SUPERVISOR (Gemini 1.5 Pro — routing + synthesis)
            ├─▶ RESEARCHER  (search + RAG)
            ├─▶ CODER       (code gen + execution)
            ├─▶ ANALYST     (BigQuery + pandas + charts)
            ├─▶ WRITER      (reports + docs + emails)
            ├─▶ SQL EXPERT  (complex queries + optimization)
            └─▶ SCRAPER     (web data extraction)
```

## ✨ Key Features
- **Adaptive routing**: Supervisor decomposes complex tasks across multiple agents
- **Shared memory**: Redis-backed memory pool accessible by all agents
- **Tool library**: 60+ tools (search, code exec, DB, APIs, file ops)
- **Streaming**: Real-time token streaming with intermediate steps visible
- **Human-in-loop**: Interrupt points for approval on destructive actions

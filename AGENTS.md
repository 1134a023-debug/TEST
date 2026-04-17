# AGENTS.md for Interactive Design Blueprint OS

Welcome, fellow AI agent! This repository contains an overarching interactive design OS project divided into several core components. 

## Sub-Projects Overview
- `mud4ai-main/`: The core Python game engine and quests for the text-based MUD4AI system.
- `網頁/`: The StellarPort Web Dashboard combining financial stock tracking with a futuristic AI UI.

## `網頁` (StellarPort) Guidelines
- **Aesthetics First**: This project heavily relies on "Glassmorphism", Neon themes, and Dark Mode. Any structural or style changes must be done in `style.css` using pure Vanilla CSS. Do NOT introduce or install frameworks like Tailwind unless explicitly requested.
- **Frontend Only Rule**: The dashboard currently runs purely on the frontend with mock data in `script.js`. The user specifically reverted the backend to avoid setup complexities. DO NOT attempt to write or start a Python backend for this directory.
- **Previewing**: To verify changes, use the `browser_subagent` to directly open the local file path: `file:///c:/新增資料夾/.../網頁/index.html`.

## `mud4ai-main` Guidelines
- This is a text-based environment in Python. Ensure any Python scripts or command lines run nicely on Windows (powershell syntax).
- Always execute operational logic from within the `mud4ai-main` directory.

## Workflows
Check out the predefined scripts in `.agents/workflows/` whenever the user asks for repetitive tasks like adding a new stock card.

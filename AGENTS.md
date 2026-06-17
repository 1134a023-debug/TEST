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

## Decision Log
- **2026-04-25**: 為了修復因 `MUDClient.cs` 缺少 `Newtonsoft.Json` 套件而產生的全域編譯錯誤，暫時將該檔案內容全部註解掉，以恢復專案儲存與腳本掛載功能。
- **2026-04-25**: 選擇使用 `PlayerPrefs` 作為場景間傳遞玩家名稱的方案，以應對 Unity 基礎作業需求。
- **2026-05-07**: 確定 `run_command` 在 Windows 主機上存在沙盒衝突 (Sandbox not supported)；決定優先提供手動執行腳本 (`.bat`) 以繞過硬體存取限制。
- **2026-05-16**: 為了避免修改現有 Unity 專案中的其他作業腳本，決定直接將彈珠台的 GameManager 重新命名為 PinballGameManager；並將發射器的發射方向從 Vector3.forward 改為 transform.forward，以相容使用者自訂的模型轉向。
## Success Log
- **2026-04-25**: 成功協助使用者完成「終極密碼」作業更新，包含名稱輸入、跨場景顯示、星星隨機縮放與場景返回功能。
- **2026-04-25**: 成功排查並解除 Unity 專案無法儲存與無法載入腳本的編譯封鎖問題。
- **2026-05-07**: 成功引導使用者完成 **Arduino UNO Q** 的初次連線、環境設定與雙核心（Linux/STM32）運作教學。
- **2026-05-14**: 成功協助使用者建立 Unity 彈珠台 (Pinball) 作業指南與 C# 腳本 (GameManager, FlipperController, MarbleCollision, Launcher)，並部署至指定 `op` 資料夾。
- **2026-05-16**: 成功引導使用者排除 Unity 彈珠台專案的腳本命名衝突 (GameManager)，並完成物理關節設定、發射器方向修正與計分機制教學。
- **2026-06-17**: 成功協助使用者完成 Unity 坦克移動與地形地物製作作業，包含製作 C# 腳本 (Player2)、編寫詳細說明書、解決地形變色、烘焙卡住與砲管穿模等問題。


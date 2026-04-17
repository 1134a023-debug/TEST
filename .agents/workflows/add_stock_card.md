---
description: How to add a new idol stock card to the StellarPort web dashboard
---

When the user asks to add or generate a new stock card, follow these steps exactly:

1. Use `view_file` to read `網頁/script.js` and locate the `mockStocks` array structure.
2. Formulate a new object literal mimicking the existing entries. It must contain the following properties: 
   - `id`: The stock symbol (e.g. '0050.TW')
   - `name`: English or Chinese name of the stock.
   - `type`: Category like 'Finance' or 'Tech'.
   - `price`: Current fake or real price string.
   - `change`: Gain or loss string (e.g. '+5.00' or '-1.20')
   - `isPositive`: boolean indicating if the change refers to a gain.
   - `aiComment`: An engaging, idol-style enthusiastic comment (using emojis like 💖 or ✨).
   - `avatarConfig`: A Dicebear avatar seed (e.g. `seed=Luna&backgroundColor=ffd5dc`)
3. Use the `multi_replace_file_content` tool to safely append this object to the `mockStocks` array.
4. Notify the user the card has been successfully added to their local JavaScript file.

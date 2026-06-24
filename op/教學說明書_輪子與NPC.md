# 坦克特效、砲彈發射與 NPC 偵測 (HW2) 製作說明書

這份說明書將指引你完成 **「射擊遊戲設計08 輪子與砲彈效果」** 與 **「射擊遊戲設計09 NPC移動偵測」** 的後續小作業設定。我們已經將所有需要的 C# 腳本建立在 `op` 資料夾中，請依照以下步驟在 Unity 中完成設定。

---

## 📹 第一階段：攝影機平滑跟隨 (PDF 08 內容)

為了防止有些 Unity 版本沒有內建 Standard Assets 或匯入時發生錯誤，**我們已直接在 `op` 資料夾中為您寫好了跟隨腳本**。您不需要再匯入材質包：

1. **取得腳本**：
   - 專案資料夾下的 [SmoothFollow.cs](file:///c:/新增資料夾/OneDrive/Desktop/_interactive_design_1_Blueprint_OS/op/SmoothFollow.cs) 即為相機平滑跟隨腳本。

2. **套用與設定**：
   - 將 **`SmoothFollow.cs`** 拖曳掛載到 Hierarchy 中的 **`Main Camera`** 物件上。
   - 點選 `Main Camera`，在右側 Inspector 的 `Smooth Follow (Script)` 中設定參數：
     - **Target (目標)**：把 Hierarchy 中的玩家坦克本體物件（例如 `Tank11` 或 `TankBody`）拖入這個欄位。
     - **Distance (距離)**：填入 `50`（與坦克的水平距離）。
     - **Height (高度)**：填入 `50`（相機高度）。
     - **Rotation Damping (旋轉平滑度)**：填入 `2`。
     - **Height Damping (高度平滑度)**：填入 `3`。
   - *測試：* 點擊 Play 執行遊戲，用鍵盤移動玩家坦克，相機就會平滑地跟著坦克移動！

---

## ⚙️ 第二階段：輪子滾動與履帶貼圖效果 (PDF 08 內容)

我們已在擴充的 `Player2.cs` 腳本中同時支援了 **「履帶貼圖捲動」** 與 **「實體輪子旋轉」** 兩種模式，你可以任選一種或同時使用：

### 模式 A：履帶坦克（材質貼圖捲動）
1. 在坦克底座左右兩側若有履帶物件，且該履帶材質的 Wrap Mode 設為 `Repeat`。
2. 點選坦克本體（掛載 `Player2.cs` 的物件），在 Inspector 中找到 **Option A: Track Renderers**：
   - 將左側的履帶 Renderer 拖入 **Track L1** / **Track L2**。
   - 將右側的履帶 Renderer 拖入 **Track R1** / **Track R2**。
   - **Track Speed** 可設為 `0.02`。
3. 執行 Play 後，坦克移動或旋轉時，履帶材質會產生流動的履帶滾動視覺效果。

### 模式 B：輪式坦克（實體輪子旋轉）
1. 在 Hierarchy 中，於坦克底座（`TankBody`）下建立 4 個 Cylinder 物件作為輪子（左右各兩個，例如命名為 `RWheel1`, `RWheel2`, `LWheel1`, `LWheel2`）。
2. 旋轉並縮放輪子，使其貼在車身兩側。
3. 點選坦克本體，在 Inspector 中找到 **Option B: Wheel GameObjects**：
   - 將右側的兩個輪子拖入 **Wheel R1** / **Wheel R2**。
   - 將左側的兩個輪子拖入 **Wheel L1** / **Wheel L2**。
   - **Wheel Rotate Speed** 設為 `100`。
4. 執行 Play 後，前進後退與轉彎時，4 個輪子會跟著對應的方向物理旋轉。

---

## 🚀 第三階段：砲彈發射與碰撞爆炸 (PDF 08 內容)

### 1. 建立砲彈發射點 (Fire)
- 在層級視窗中，點開你的坦克砲管物件（例如 `Tank11_Can`），**右鍵建立一個空物件 (Create Empty)**，命名為 **`Fire`**。
- 將 `Fire` 物件移動到砲管的最前端（砲口位置），並確保它的藍色箭頭（Z 軸朝前）指向砲彈飛出的方向。
- 將 `op/Fire.cs` 腳本掛載到該 **`Fire`** 物件上。

### 2. 製作砲彈 Prefab
- 在 Hierarchy 視窗 `右鍵 -> 3D Object -> Sphere` 建立一個球體，命名為 `Sphere`。
- 修改其 Scale 大小（例如 X: 0.4, Y: 0.4, Z: 0.4），使其符合砲彈大小。
- 點選該 Sphere，在 Inspector 點擊 `Add Component -> Physics -> Rigidbody` (鋼體)。
- 將 `op/Fired.cs` 腳本拖曳掛載到該 `Sphere` 上。
- **製作成 Prefab**：在專案 Assets 中建立一個 `Prefabs` 資料夾，將 Hierarchy 中的 `Sphere` 物件**拖入專案視窗中**。此時 Hierarchy 中的 Sphere 會變成藍色，代表已成為 Prefab。
- **刪除場景中的 Sphere**：刪除 Hierarchy 中的那顆 `Sphere`（因為發射時才會動態生成，場景中一開始不需要有）。

### 3. 設定發射與爆炸關聯
- **發射關聯**：點選砲管前端的 `Fire` 物件，在 `Fire (Script)` 元件的 **`Projectile`** 欄位中，把剛剛製作的 **`Sphere Prefab`** 拖入。
- **爆炸效果關聯**：
  - 點選上方選單 `Assets -> Import Package -> ParticleSystems` 匯入爆炸粒子。
  - 匯入後，在專案視窗的 `Standard Assets -> ParticleSystems -> Prefabs` 下會找到 **`Explosion`** 粒子預製體。
  - 點選專案 Assets 中的 **`Sphere Prefab`**，在 Inspector 的 `Fired (Script)` 元件中，將 **`Explosion`** 粒子預製體拖入 **`Explosion`** 欄位。
- *測試：* 執行 Play，按下滑鼠左鍵或鍵盤左 Ctrl 鍵，砲彈會從砲口飛出；撞擊到地面或障礙物時會產生爆炸煙火特效並自我銷毀。

---

## 🤖 第四階段：NPC 巡邏與 Raycast 偵測 (PDF 09 內容)

1. **建立 NPC 坦克**：
   - 複製（`Ctrl + D`）你的玩家坦克，將其改名為 **`Enemy`**，並移動到場景中較遠的另一個位置。
   - **移除玩家控制**：移除該 Enemy 物件上的 `Player2.cs` 腳本與 `Fire` 子物件上的 `Fire.cs` 腳本（避免 NPC 也被玩家鍵盤控制）。
   - **確認玩家標籤**：選取玩家坦克本體，確保其 Inspector 最上方的 **`Tag`** 被設定為 **`Player`**（NPC 是透過這個標籤來辨認玩家的）。

2. **掛載 NPC AI 控制**：
   - 將 `op/Enemy.cs` 腳本掛載到該 **`Enemy` (NPC 坦克底座)** 上。
   - 點選 `Enemy` 坦克，在 Inspector 中設定：
     - **Bullet** 欄位：將專案中的 **`Sphere Prefab`** (砲彈) 拖入。

3. **偵測與行為測試**：
   - 點擊 Play 執行遊戲。
   - **巡邏狀態**：在玩家尚未靠近時，NPC 坦克會自動往前行駛 200 步，接著在原地旋轉 180 度，重複前進與旋轉以進行巡邏。
   - 在編輯器 Scene 視窗中，你可以看到一條**紅色的偵測射線 (DrawRay)** 從 NPC 坦克前方射出。
   - **觸發射擊**：開著玩家坦克駛入該紅色射線範圍內（50米內），NPC 坦克會立刻停下，並每隔 2 秒朝你發射一顆砲彈！

---

## 📝 繳交檢查清單
- [ ] 相機掛載了 `SmoothFollow.cs` 並平滑跟隨玩家坦克。
- [ ] 坦克履帶有貼圖流動捲動（Option A）或 4 個車輪有物理滾動（Option B）。
- [ ] 砲管前端設有發射點 `Fire` 物件，並掛載 `Fire.cs`；按下滑鼠左鍵能射出砲彈。
- [ ] 砲彈撞擊到地形或障礙物時會產生爆炸特效並銷毀，且發射時坦克不會因為物理碰撞而彈開。
- [ ] 場景中至少有一台掛載 `Enemy.cs` 的 NPC 坦克，會在無玩家時巡邏，偵測到玩家（Tag 為 Player）時停下並開火射擊。

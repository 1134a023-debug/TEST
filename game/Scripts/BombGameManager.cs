using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class BombGameManager : MonoBehaviour
{
    [Header("UI 參考 (請將畫面上的 Text 元件拖拉到這裡)")]
    public Text inputDisplayText; // 顯示玩家輸入的數字
    public Text hintText;         // 顯示範圍提示
    public Text attemptsText;     // 顯示剩餘次數
    public Text nameDisplayText; // 顯示玩家名稱 (新增)

    [Header("遊戲設定")]
    public int maxAttempts = 5;               // 最大猜測次數
    public string endSceneName = "EndScene";  // 結束場景的名稱

    private int targetNumber;
    private string currentInputString = "";
    
    private int remainingAttempts;
    private int minRange = 0;
    private int maxRange = 99;

    private void Start()
    {
        // 亂數產生炸彈密碼
        targetNumber = Random.Range(1, 100);
        remainingAttempts = maxAttempts;
        
        UpdateUI();
        
        // 讀取並顯示玩家名稱 (新增)
        string playerName = PlayerPrefs.GetString("PlayerName", "玩家");
        nameDisplayText.text = $"玩家: {playerName}";
        
        hintText.text = $"請輸入 {minRange} 到 {maxRange} 之間的數字。";
    }

    // 這個方法要給 0~9 的按鈕使用 (在 Button 的 OnClick 中呼叫，並填入 0~9 參數)
    public void OnNumberClicked(int number)
    {
        currentInputString += number.ToString();
        
        // 限制最多只能輸入兩位數 (例如 99)
        if (currentInputString.Length > 2)
        {
            currentInputString = currentInputString.Substring(0, 2);
        }
        UpdateUI();
    }

    // 給 Clear(清除) 按鈕使用
    public void OnClearClicked()
    {
        currentInputString = "";
        UpdateUI();
    }

    // 給 Submit(送出/確認) 按鈕使用
    public void OnSubmitClicked()
    {
        // 如果沒有輸入就按送出，直接 return 不處理
        if (string.IsNullOrEmpty(currentInputString)) return;

        int guess = int.Parse(currentInputString);
        remainingAttempts--;

        if (guess == targetNumber)
        {
            // 猜中了！ (拆除炸彈)
            PlayerPrefs.SetInt("GameResult", 1); // 1 代表勝利
            PlayerPrefs.Save();
            SceneManager.LoadScene(endSceneName); // 載入結束畫面
            return;
        }
        else
        {
            // 猜錯了，更新範圍
            if (guess > targetNumber)
            {
                if (guess < maxRange) maxRange = guess;
                hintText.text = $"嗶嗶！太大！介於 {minRange} 到 {maxRange}";
            }
            else
            {
                if (guess > minRange) minRange = guess;
                hintText.text = $"嗶嗶！太小！介於 {minRange} 到 {maxRange}";
            }
        }

        // 清空輸入並更新畫面
        currentInputString = "";
        UpdateUI();

        // 判斷是否沒有剩餘次數 (爆炸)
        if (remainingAttempts <= 0)
        {
            PlayerPrefs.SetInt("GameResult", 0); // 0 代表失敗
            PlayerPrefs.Save();
            SceneManager.LoadScene(endSceneName);
        }
    }

    private void UpdateUI()
    {
        inputDisplayText.text = currentInputString == "" ? "0" : currentInputString;
        attemptsText.text = $"剩餘次數: {remainingAttempts}";
    }

    // 返回主場景的功能 (新增)
    public void OnBackToMainScene()
    {
        SceneManager.LoadScene("LoadingScene");
    }
}

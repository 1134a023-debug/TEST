using UnityEngine;
using UnityEngine.UI; // 改用一般的 UI 函式庫，支援內建中文

public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    public int score = 0;
    public Text scoreText; // 改回 Legacy Text 支援中文

    void Awake()
    {
        // 設定這個腳本為唯一實例
        if (instance == null)
            instance = this;
    }

    // 這個方法給 PinController 呼叫來加分
    public void AddScore()
    {
        score += 1;
        Debug.Log("成功觸發加分！目前分數：" + score);

        // 如果有綁定文字 UI，就更新畫面
        if (scoreText != null)
        {
            scoreText.text = "分數: " + score;
        }
        else
        {
            Debug.LogWarning("⚠️ 警告：GameManager 裡面的 Score Text 欄位是空的，請把 UI 拖進去！");
        }
    }

    public void QuitGame()
    {
        Debug.Log("遊戲結束！");
        Application.Quit();
    }
}

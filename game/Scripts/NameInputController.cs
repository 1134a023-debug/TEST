using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class NameInputController : MonoBehaviour
{
    [Header("UI 參考")]
    public InputField nameInputField; // 拖曳 InputField 到這裡
    public string nextSceneName = "CalculatorUIScene";

    // 讓按鈕呼叫這個函式
    public void StartGame()
    {
        string playerName = nameInputField.text;

        if (string.IsNullOrEmpty(playerName))
        {
            playerName = "無名玩家";
        }

        // 將名稱存入 PlayerPrefs，以便跨場景使用
        PlayerPrefs.SetString("PlayerName", playerName);
        PlayerPrefs.Save();

        Debug.Log($"玩家名稱: {playerName}，準備開始遊戲！");
        SceneManager.LoadScene(nextSceneName);
    }
}

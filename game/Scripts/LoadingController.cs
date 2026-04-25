using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadingController : MonoBehaviour
{
    [Header("場景設定")]
    [Tooltip("核心遊戲場景的名稱")]
    public string nextSceneName = "CalculatorUIScene";

    // 讓按鈕去呼叫這個函式來開始遊戲
    public void StartGame()
    {
        Debug.Log("準備切換到炸彈場景！");
        SceneManager.LoadScene(nextSceneName);
    }
}

using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class EndSceneController : MonoBehaviour
{
    [Header("UI 參考")]
    public Image resultImage; // 用來切換圖片的 Image 元件

    [Header("圖片資源設定")]
    public Sprite winSprite;  // 勝利的圖片 (拆除成功)
    public Sprite loseSprite; // 失敗的圖片 (炸彈爆炸)

    private void Start()
    {
        // 讀取上一關存下來的結果，預設為 0 (失敗)
        int result = PlayerPrefs.GetInt("GameResult", 0);
        
        if (result == 1)
        {
            // 勝利！更換成勝利的圖片
            resultImage.sprite = winSprite;
        }
        else
        {
            // 失敗！更換成爆炸的圖片
            resultImage.sprite = loseSprite;
        }
    }

    // 可選：可以拉一個「重新開始」的按鈕呼叫這個方法
    public void OnRestartClicked()
    {
        // 通常重新開始會回到第一個畫面(請替換成你的第一個 Scene 名稱)
        SceneManager.LoadScene("LoadingScene"); 
    }
}

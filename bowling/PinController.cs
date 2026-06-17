using UnityEngine;

public class PinController : MonoBehaviour
{
    private bool isFallen = false;

    void Update()
    {
        // 如果瓶子還沒倒下，就持續檢查它的傾斜角度
        if (!isFallen)
        {
            // Vector3.Angle 會計算瓶子的「上方」和真實世界的「正上方」差了幾度
            // 如果大於 45 度，我們就判定它倒了
            if (Vector3.Angle(Vector3.up, transform.up) > 45f)
            {
                isFallen = true; // 標記為已倒下，避免重複加分
                Debug.Log("瓶子倒下了！");
                
                // 通知 GameManager 加 1 分
                if (GameManager.instance != null)
                {
                    GameManager.instance.AddScore();
                }
                else
                {
                    Debug.LogError("找不到 GameManager！");
                }
            }
        }
    }
}

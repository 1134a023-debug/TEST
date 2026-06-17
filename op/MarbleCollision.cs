using UnityEngine;

public class MarbleCollision : MonoBehaviour
{
    private PinballGameManager gm;

    void Start()
    {
        gm = FindObjectOfType<PinballGameManager>();
    }

    // 處理觸發器 (黑洞)
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("BlackHole"))
        {
            if (gm != null)
            {
                gm.DeductScore(500); // 掉入黑洞扣 500 分
            }
            // 讓彈珠回到發射點，或是直接結束遊戲
            Destroy(gameObject); 
        }
    }

    // 處理實體碰撞 (計分道具)
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("ScoreItem"))
        {
            if (gm != null)
            {
                gm.AddScore(100); // 撞到道具加 100 分
            }
        }
    }
}

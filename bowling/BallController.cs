using UnityEngine;
using UnityEngine.UI;

public class BallController : MonoBehaviour
{
    public float throwForce = 1500f;
    private Rigidbody rb;
    private bool hasThrown = false;
    
    [Header("UI 連結")]
    public Slider angleSlider; // 拖入畫面上的 Slider

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        // 如果還沒丟球，球的 X 軸位置跟隨 Slider 的值移動
        if (!hasThrown && angleSlider != null)
        {
            Vector3 pos = transform.position;
            pos.x = angleSlider.value;
            transform.position = pos;
        }
    }

    public void ThrowBall()
    {
        if (!hasThrown)
        {
            // 將 Slider 隱藏或停用
            if (angleSlider != null) angleSlider.gameObject.SetActive(false);
            
            rb.AddForce(Vector3.forward * throwForce);
            hasThrown = true;
        }
    }
}

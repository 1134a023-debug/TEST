using UnityEngine;

public class Launcher : MonoBehaviour
{
    public float maxPower = 2000f;
    public float chargeRate = 1000f;
    private float currentPower = 0f;
    
    public Rigidbody marbleRb; // 在 Inspector 中放入彈珠
    private bool isCharging = false;
    private Vector3 initialPosition;

    void Start()
    {
        initialPosition = transform.position;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            isCharging = true;
            currentPower = 0f;
        }

        if (Input.GetKey(KeyCode.Space) && isCharging)
        {
            currentPower += chargeRate * Time.deltaTime;
            currentPower = Mathf.Clamp(currentPower, 0, maxPower);
            
            // 讓推桿稍微往後退，產生蓄力視覺效果
            transform.Translate(Vector3.back * Time.deltaTime * 0.5f);
        }

        if (Input.GetKeyUp(KeyCode.Space) && isCharging)
        {
            // 將力量施加給彈珠 (依照發射器的正前方)
            if (marbleRb != null)
            {
                marbleRb.AddForce(transform.forward * currentPower);
            }
            
            // 推桿回到原位
            transform.position = initialPosition;
            isCharging = false;
        }
    }
}

using UnityEngine;

public class SmoothFollow : MonoBehaviour
{
    [Header("Follow Target")]
    public Transform target;            // 相機要跟隨的目標 (拖入玩家坦克)

    [Header("Position Settings")]
    public float distance = 10.0f;      // 與目標的水平距離
    public float height = 5.0f;          // 與目標的高度差

    [Header("Damping (Smoothness)")]
    public float heightDamping = 2.0f;    // 高度跟隨平滑度
    public float rotationDamping = 3.0f;  // 旋轉跟隨平滑度

    void LateUpdate()
    {
        // 如果沒有設定目標，就不執行跟隨
        if (!target) return;

        // 計算目標的預期旋轉角度與高度
        float wantedRotationAngle = target.eulerAngles.y;
        float wantedHeight = target.position.y + height;

        // 取得相機當前的旋轉角度與高度
        float currentRotationAngle = transform.eulerAngles.y;
        float currentHeight = transform.position.y;

        // 使用插值 (Lerp) 讓相機的 Y 軸旋轉與高度漸進式改變，達到平滑效果
        currentRotationAngle = Mathf.LerpAngle(currentRotationAngle, wantedRotationAngle, rotationDamping * Time.deltaTime);
        currentHeight = Mathf.Lerp(currentHeight, wantedHeight, heightDamping * Time.deltaTime);

        // 將旋轉角度轉換為四元數旋轉
        Quaternion currentRotation = Quaternion.Euler(0, currentRotationAngle, 0);

        // 設定相機在 X-Z 平面的位置（距離目標後方 distance 距離）
        transform.position = target.position;
        transform.position -= currentRotation * Vector3.forward * distance;

        // 設定相機的高度
        transform.position = new Vector3(transform.position.x, currentHeight, transform.position.z);

        // 讓相機始終看向目標坦克
        transform.LookAt(target);
    }
}

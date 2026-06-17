using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player2 : MonoBehaviour {
    [Header("Tank Status")]
    public int Hp = 3;

    [Header("Tank GameObjects")]
    public GameObject TankBody;      // 坦克車本體 (底座)
    public GameObject TankTop;       // 坦克砲塔
    public GameObject TankEmitter;   // 坦克砲管 (請拖入 BarrelPivot 空物件)

    [Header("Movement & Rotation Speeds")]
    public float MoveSpeed = 5f;            // 前進後退速度 (每秒公尺)
    public float BodyRotateSpeed = 90f;     // 車身旋轉速度 (每秒度數)
    public float TurretRotateSpeed = 60f;   // 砲塔旋轉速度 (每秒度數)
    public float EmitterPitchSpeed = 30f;   // 砲管俯仰速度 (每秒度數)

    [Header("Pitch Angle Limits")]
    public float MaxPitchUp = 45f;          // 最大仰角
    public float MaxPitchDown = -5f;        // 最大俯角 (設為 0 或 -5 可以防止砲管插地)

    [Header("Turret Rotation Limits")]
    public float MaxTurretAngle = 135f;     // 砲塔單邊旋轉最大角度 (預設 135 度，左右合計 270 度)

    private float anglenow = 0f;            // 記錄砲管目前的俯仰角度 (改為 float)
    private float turretYawNow = 0f;        // 記錄砲塔目前的左右旋轉角度

    // Use this for initialization
    void Start () {
        // 初始化檢查，若未手動拖曳則自動尋找
        if (TankBody == null) TankBody = this.gameObject;
    }
    
    // Update is called once per frame
    void Update () {
        // --- 1. 坦克車本體移動 (W: 前進, S: 後退) ---
        if (Input.GetKey(KeyCode.W)) {
            TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * MoveSpeed, Space.World);
        }
        if (Input.GetKey(KeyCode.S)) {
            TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * -MoveSpeed, Space.World);
        }

        // --- 2. 坦克車本體旋轉 (A: 左轉, D: 右轉) ---
        if (Input.GetKey(KeyCode.A)) {
            TankBody.transform.Rotate(new Vector3(0, -1, 0) * Time.deltaTime * BodyRotateSpeed);
        }
        if (Input.GetKey(KeyCode.D)) {
            TankBody.transform.Rotate(new Vector3(0, 1, 0) * Time.deltaTime * BodyRotateSpeed);
        }

        // --- 3. 砲塔旋轉 (Q: 左旋, E: 右旋) ---
        if (TankTop != null) {
            // Q 鍵左旋 (角度減少)
            if (Input.GetKey(KeyCode.Q)) {
                if (turretYawNow > -MaxTurretAngle) {
                    float rotateStep = TurretRotateSpeed * Time.deltaTime;
                    TankTop.transform.Rotate(new Vector3(0, -1, 0) * rotateStep);
                    turretYawNow -= rotateStep;
                }
            }
            // E 鍵右旋 (角度增加)
            if (Input.GetKey(KeyCode.E)) {
                if (turretYawNow < MaxTurretAngle) {
                    float rotateStep = TurretRotateSpeed * Time.deltaTime;
                    TankTop.transform.Rotate(new Vector3(0, 1, 0) * rotateStep);
                    turretYawNow += rotateStep;
                }
            }
        }

        // --- 4. 砲管俯仰角調整 (R: 抬高砲管, F: 降低砲管) ---
        if (TankEmitter != null) {
            // 抬高砲管
            if (Input.GetKey(KeyCode.R)) {
                if (anglenow < MaxPitchUp) {
                    float rotateStep = EmitterPitchSpeed * Time.deltaTime;
                    TankEmitter.transform.Rotate(new Vector3(1, 0, 0) * rotateStep);
                    anglenow += rotateStep;
                }
            }
            // 降低砲管
            if (Input.GetKey(KeyCode.F)) {
                if (anglenow > MaxPitchDown) {
                    float rotateStep = EmitterPitchSpeed * Time.deltaTime;
                    TankEmitter.transform.Rotate(new Vector3(-1, 0, 0) * rotateStep);
                    anglenow -= rotateStep;
                }
            }
        }
    }
}

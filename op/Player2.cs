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

    private float anglenow = 0f;            // 記錄砲管目前的俯仰角度 (改為 float)

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
            if (Input.GetKey(KeyCode.Q)) {
                TankTop.transform.Rotate(new Vector3(0, -1, 0) * Time.deltaTime * TurretRotateSpeed);
            }
            if (Input.GetKey(KeyCode.E)) {
                TankTop.transform.Rotate(new Vector3(0, 1, 0) * Time.deltaTime * TurretRotateSpeed);
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

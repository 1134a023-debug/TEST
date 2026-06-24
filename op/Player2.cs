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

    [Header("Option A: Track Renderers (Tracked Tank)")]
    public Renderer trackR1;
    public Renderer trackR2;
    public Renderer trackL1;
    public Renderer trackL2;

    [Header("Option B: Wheel GameObjects (Wheeled Tank)")]
    public GameObject WheelR1;
    public GameObject WheelR2;
    public GameObject WheelL1;
    public GameObject WheelL2;

    [Header("Track & Wheel Speeds")]
    public float trackSpeed = 0.02f;        // 履帶貼圖滾動速度
    public float wheelRotateSpeed = 100f;   // 輪子旋轉速度

    // Use this for initialization
    void Start () {
        // 初始化檢查，若未手動拖曳則自動尋找
        if (TankBody == null) TankBody = this.gameObject;
    }
    
    // Update is called once per frame
    void Update () {
        // --- 0. 取得履帶貼圖滾動偏移量 (若有設定履帶才進行) ---
        bool hasTracks = (trackL1 != null && trackL2 != null && trackR1 != null && trackR2 != null);
        bool hasWheels = (WheelL1 != null && WheelL2 != null && WheelR1 != null && WheelR2 != null);

        Vector2 L1offset = hasTracks ? trackL1.material.mainTextureOffset : Vector2.zero;
        Vector2 L2offset = hasTracks ? trackL2.material.mainTextureOffset : Vector2.zero;
        Vector2 R1offset = hasTracks ? trackR1.material.mainTextureOffset : Vector2.zero;
        Vector2 R2offset = hasTracks ? trackR2.material.mainTextureOffset : Vector2.zero;

        Rigidbody rb = TankBody.GetComponent<Rigidbody>();

        // --- 1. 坦克車本體移動 (W: 前進, S: 後退) ---
        if (Input.GetKey(KeyCode.W)) {
            if (rb != null && !rb.isKinematic) {
                rb.MovePosition(rb.position + TankBody.transform.forward * Time.deltaTime * MoveSpeed);
            } else {
                TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * MoveSpeed, Space.World);
            }

            if (hasTracks) {
                L1offset.y += trackSpeed;
                L2offset.y += trackSpeed;
                R1offset.y += trackSpeed;
                R2offset.y += trackSpeed;
            }
            if (hasWheels) {
                float rotateStep = wheelRotateSpeed * Time.deltaTime;
                WheelR1.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelR2.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelL1.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelL2.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
            }
        }
        if (Input.GetKey(KeyCode.S)) {
            if (rb != null && !rb.isKinematic) {
                rb.MovePosition(rb.position + TankBody.transform.forward * Time.deltaTime * -MoveSpeed);
            } else {
                TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * -MoveSpeed, Space.World);
            }

            if (hasTracks) {
                L1offset.y -= trackSpeed;
                L2offset.y -= trackSpeed;
                R1offset.y -= trackSpeed;
                R2offset.y -= trackSpeed;
            }
            if (hasWheels) {
                float rotateStep = wheelRotateSpeed * Time.deltaTime;
                WheelR1.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelR2.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelL1.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelL2.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
            }
        }

        // --- 2. 坦克車本體旋轉 (A: 左轉, D: 右轉) ---
        if (Input.GetKey(KeyCode.A)) {
            if (rb != null && !rb.isKinematic) {
                Quaternion deltaRotation = Quaternion.Euler(new Vector3(0, -1, 0) * Time.deltaTime * BodyRotateSpeed);
                rb.MoveRotation(rb.rotation * deltaRotation);
            } else {
                TankBody.transform.Rotate(new Vector3(0, -1, 0) * Time.deltaTime * BodyRotateSpeed);
            }

            if (hasTracks) {
                L1offset.y -= trackSpeed;
                L2offset.y -= trackSpeed;
                R1offset.y += trackSpeed;
                R2offset.y += trackSpeed;
            }
            if (hasWheels) {
                float rotateStep = wheelRotateSpeed * Time.deltaTime;
                WheelR1.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelR2.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelL1.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelL2.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
            }
        }
        if (Input.GetKey(KeyCode.D)) {
            if (rb != null && !rb.isKinematic) {
                Quaternion deltaRotation = Quaternion.Euler(new Vector3(0, 1, 0) * Time.deltaTime * BodyRotateSpeed);
                rb.MoveRotation(rb.rotation * deltaRotation);
            } else {
                TankBody.transform.Rotate(new Vector3(0, 1, 0) * Time.deltaTime * BodyRotateSpeed);
            }

            if (hasTracks) {
                L1offset.y += trackSpeed;
                L2offset.y += trackSpeed;
                R1offset.y -= trackSpeed;
                R2offset.y -= trackSpeed;
            }
            if (hasWheels) {
                float rotateStep = wheelRotateSpeed * Time.deltaTime;
                WheelR1.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelR2.transform.Rotate(new Vector3(0, -1, 0), rotateStep);
                WheelL1.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
                WheelL2.transform.Rotate(new Vector3(0, 1, 0), rotateStep);
            }
        }

        // --- 2.5 套用履帶貼圖捲動偏移量 ---
        if (hasTracks) {
            trackL1.material.mainTextureOffset = L1offset;
            trackL2.material.mainTextureOffset = L2offset;
            trackR1.material.mainTextureOffset = R1offset;
            trackR2.material.mainTextureOffset = R2offset;
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

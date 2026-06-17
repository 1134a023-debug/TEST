using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player2 : MonoBehaviour {
    [Header("Tank Status")]
    public int Hp = 3;

    [Header("Tank GameObjects")]
    public GameObject TankBody;      // 坦克車本體 (底座)
    public GameObject TankTop;       // 坦克砲塔
    public GameObject TankEmitter;   // 坦克砲管

    [Header("Pitch Angle Limits")]
    public int MaxPitchUp = 45;      // 最大仰角
    public int MaxPitchDown = -5;    // 最大俯角 (設為 0 或 -5 可以防止砲管插地)

    private int anglenow = 0;        // 記錄砲管目前的俯仰角度

    // Use this for initialization
    void Start () {
        // 初始化檢查，若未手動拖曳則自動尋找
        if (TankBody == null) TankBody = this.gameObject;
    }
    
    // Update is called once per frame
    void Update () {
        // --- 1. 坦克車本體移動 (W: 前進, S: 後退) ---
        if (Input.GetKey(KeyCode.W)) {
            TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * 5, Space.World);
        }
        if (Input.GetKey(KeyCode.S)) {
            TankBody.transform.Translate(TankBody.transform.forward * Time.deltaTime * -5, Space.World);
        }

        // --- 2. 坦克車本體旋轉 (A: 左轉, D: 右轉) ---
        if (Input.GetKey(KeyCode.A)) {
            TankBody.transform.Rotate(new Vector3(0, -1, 0), 1);
        }
        if (Input.GetKey(KeyCode.D)) {
            TankBody.transform.Rotate(new Vector3(0, 1, 0), 1);
        }

        // --- 3. 砲塔旋轉 (Q: 左旋, E: 右旋) ---
        if (TankTop != null) {
            if (Input.GetKey(KeyCode.Q)) {
                TankTop.transform.Rotate(new Vector3(0, -1, 0), 1);
            }
            if (Input.GetKey(KeyCode.E)) {
                TankTop.transform.Rotate(new Vector3(0, 1, 0), 1);
            }
        }

        // --- 4. 砲管俯仰角調整 (R: 抬高砲管, F: 降低砲管) ---
        if (TankEmitter != null) {
            // 抬高砲管
            if (Input.GetKey(KeyCode.R)) {
                if (anglenow < MaxPitchUp) {
                    TankEmitter.transform.Rotate(new Vector3(1, 0, 0), 1);
                    anglenow++;
                }
            }
            // 降低砲管
            if (Input.GetKey(KeyCode.F)) {
                if (anglenow > MaxPitchDown) {
                    TankEmitter.transform.Rotate(new Vector3(-1, 0, 0), 1);
                    anglenow--;
                }
            }
        }
    }
}

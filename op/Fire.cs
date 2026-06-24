using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fire : MonoBehaviour {
    [Header("Shell Prefab")]
    public Rigidbody projectile;     // 砲彈的 Prefab (需帶有 Rigidbody 與 Collider)

    [Header("Shooting Speed")]
    public float speed = 80f;        // 砲彈發射初速度

    // Use this for initialization
    void Start () {
        
    }
    
    // Update is called once per frame
    void Update () {
        // 當按下 Fire1 (預設為滑鼠左鍵或鍵盤 Left Ctrl)
        if (Input.GetButtonDown("Fire1")) {
            if (projectile != null) {
                // 在發射點 (Fire 物件) 的位置與旋轉方向實例化生成砲彈
                Rigidbody shoot = Instantiate(projectile, transform.position, transform.rotation) as Rigidbody;
                
                // 設定砲彈往前飛的速度向量
                shoot.velocity = transform.TransformDirection(new Vector3(0, 0, speed));
                
                // 防止砲彈與發射它的坦克自身發生碰撞，造成坦克彈飛或翻車
                Collider tankCollider = transform.root.GetComponent<Collider>();
                Collider bulletCollider = shoot.GetComponent<Collider>();
                if (tankCollider != null && bulletCollider != null) {
                    Physics.IgnoreCollision(tankCollider, bulletCollider);
                }
            } else {
                Debug.LogWarning("未指定砲彈 Prefab (projectile)！請將製作好的砲彈拉入 Inspector 中。");
            }
        }
    }
}

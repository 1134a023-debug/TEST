using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour {
    private bool targetfound = false;
    private bool forward = true;
    private bool turn = false;
    private int linearcount = 0;
    private int angularcount = 0;
    private RaycastHit hit;

    private float period1;
    private float period2;

    [Header("Bullet Prefab")]
    public GameObject bullet;        // 砲彈 Prefab (通常是與 Player 相同的 Sphere Prefab)

    // Use this for initialization
    void Start () {
        period1 = Time.time;
    }
    
    // Update is called once per frame
    void Update () {
        // 在編輯器中畫出紅色偵測射線，方便觀察 NPC 偵測範圍 (長度 50)
        Debug.DrawRay(transform.position, transform.forward * 50.0f, Color.red);

        // --- 1. 自動巡邏行為 (未偵測到玩家時) ---
        if (!targetfound) {
            // 往前走 200 步
            if (linearcount < 200 && forward) {
                // 沿著坦克的前方移動 (與 PDF 09 投影片相同)
                transform.Translate(transform.forward * 0.125f, Space.World);
                linearcount++;
            }
            
            // 走滿 200 步，切換至迴轉狀態
            if (linearcount == 200 && !turn) {
                turn = true;
                forward = false;
            }
            
            // 原地旋轉 180 度 (每次旋轉 2 度，旋轉 90 次為 180 度)
            if (turn) {
                transform.Rotate(new Vector3(0, 1, 0), 2.0f);
                angularcount++;
                if (angularcount == 90) {
                    angularcount = 0;
                    linearcount = 0;
                    forward = true;
                    turn = false;
                }
            }
        }

        // --- 2. 射線探測玩家 (Physics.Raycast) ---
        // 從坦克中心朝正前方 (transform.forward) 發射一條長度 50.0f 的射線
        if (Physics.Raycast(transform.position, transform.forward, out hit, 50.0f)) {
            // 如果射線打中的物件 Tag 為 "Player"
            if (hit.collider.gameObject.CompareTag("Player")) {
                period2 = Time.time;
                
                // 發射間隔冷卻限制為 2 秒
                if (period2 - period1 > 2.0f) {
                    targetfound = true;
                    
                    if (bullet != null) {
                        // 實例化生成砲彈
                        GameObject newBullet = (GameObject)Instantiate(bullet);
                        
                        // 設定砲彈初始位置在坦克位置 (稍微往外偏移一點，防止在坦克正中心生成導致物理穿模)
                        newBullet.transform.position = transform.position + transform.forward * 2.0f;
                        
                        // 取得砲彈鋼體並給予推進力
                        Rigidbody rb = newBullet.GetComponent<Rigidbody>();
                        if (rb != null) {
                            // 1. 投影片原始邏輯 (以自身位置座標作為力向量)：
                            rb.AddForce(gameObject.transform.position);
                            
                            // 2. 修正補強邏輯 (朝坦克正前方給予推力，確保砲彈必定朝玩家方向射出)：
                            rb.AddForce(transform.forward * 1500f);
                        }
                        
                        // 忽略 NPC 與自己射出砲彈的碰撞，防止 NPC 坦克自己翻車
                        Collider enemyCollider = GetComponent<Collider>();
                        Collider bulletCollider = newBullet.GetComponent<Collider>();
                        if (enemyCollider != null && bulletCollider != null) {
                            Physics.IgnoreCollision(enemyCollider, bulletCollider);
                        }
                    }
                    
                    period1 = Time.time;
                }
            } else {
                targetfound = false;
            }
        } else {
            targetfound = false;
        }
    }
}

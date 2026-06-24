using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fired : MonoBehaviour {
    [Header("Explosion Particle Prefab")]
    public GameObject explosion;     // 爆炸粒子特效 (Explosion Prefab)

    // Use this for initialization
    void Start () {
        
    }
    
    // Update is called once per frame
    void Update () {
        
    }

    // 當碰撞體與其他物件發生碰撞時觸發
    void OnCollisionEnter(Collision collision) {
        if (explosion != null) {
            // 在砲彈當前撞擊位置生成爆炸特效
            Instantiate(explosion, transform.position, transform.rotation);
        }
        
        // 銷毀砲彈本體
        Destroy(gameObject);
    }
}

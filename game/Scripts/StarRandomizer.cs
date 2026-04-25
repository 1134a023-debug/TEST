using UnityEngine;

public class StarRandomizer : MonoBehaviour
{
    [Header("縮放設定")]
    public float minScale = 0.5f;
    public float maxScale = 2.0f;

    void Start()
    {
        RandomizeSize();
    }

    // 每次物件啟用時也可以隨機化 (如果星星是重複使用的)
    void OnEnable()
    {
        RandomizeSize();
    }

    public void RandomizeSize()
    {
        float randomScale = Random.Range(minScale, maxScale);
        transform.localScale = new Vector3(randomScale, randomScale, 1f);
        
        // 可選：隨機旋轉
        transform.rotation = Quaternion.Euler(0, 0, Random.Range(0f, 360f));
        
        Debug.Log($"{gameObject.name} 的隨機縮放值: {randomScale}");
    }
}

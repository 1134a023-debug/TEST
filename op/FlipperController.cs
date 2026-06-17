using UnityEngine;

[RequireComponent(typeof(HingeJoint))]
public class FlipperController : MonoBehaviour
{
    public float hitForce = 10000f;
    public float flipperDamper = 150f;
    public bool isLeftFlipper = true; // 在 Inspector 中打勾代表左擋板
    
    private HingeJoint hinge;
    private JointSpring springConfig;

    void Start()
    {
        hinge = GetComponent<HingeJoint>();
        hinge.useSpring = true;
        
        springConfig = new JointSpring();
        springConfig.spring = hitForce;
        springConfig.damper = flipperDamper;
        
        // 初始狀態：退回原位
        springConfig.targetPosition = 0;
        hinge.spring = springConfig;
    }

    void Update()
    {
        bool isPressed = false;

        if (isLeftFlipper && Input.GetKey(KeyCode.LeftArrow))
        {
            isPressed = true;
        }
        else if (!isLeftFlipper && Input.GetKey(KeyCode.RightArrow))
        {
            isPressed = true;
        }

        if (isPressed)
        {
            springConfig.targetPosition = isLeftFlipper ? -45f : 45f;
        }
        else
        {
            springConfig.targetPosition = 0f;
        }

        hinge.spring = springConfig;
    }
}

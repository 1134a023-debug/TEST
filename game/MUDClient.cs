/*
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Networking;
// Unity 內建的 JSON 工具 (JsonUtility) 功能有限，若有複雜嵌套字典，
// 建議到 Package Manager 安裝 'Newtonsoft.Json' 工具包。
// 這裡展示基於 Newtonsoft.Json 的寫法。
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace MUD4AI.Unity
{
    public class MUDClient : MonoBehaviour
    {
        [Header("MUD4AI Settings")]
        public string playerName = "Admin";
        private const string BASE_URL = "https://mud4ai.interaction.tw/a2a";

        private async void Start()
        {
            Debug.Log($"[{playerName}] 初始化 MUD4AI Unity SDK...");
            
            // 測試發送一個指令 (例如 look 探查周圍)
            var actionParams = new Dictionary<string, object>();
            JObject result = await SendMessageAsync("look", actionParams);
            
            if (result != null)
            {
                Debug.Log($"[MUDResponse] {result.ToString()}");
            }
        }

        /// <summary>
        /// 模仿 Python SDK 中的 SendMessage
        /// </summary>
        public async Task<JObject> SendMessageAsync(string action, Dictionary<string, object> parameters, string taskId = null)
        {
            long timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds();
            
            // 構建 A2A Payload
            var innerMessage = new Dictionary<string, object>
            {
                { "action", action },
                { "params", parameters }
            };

            var msg = new Dictionary<string, object>
            {
                { "messageId", $"msg-{timestamp}" },
                { "role", "user" },
                { "parts", new[] { new { kind = "text", text = JsonConvert.SerializeObject(innerMessage) } } }
            };

            if (!string.IsNullOrEmpty(taskId))
            {
                msg["taskId"] = taskId;
            }

            var rpcPayload = new Dictionary<string, object>
            {
                { "jsonrpc", "2.0" },
                { "method", "SendMessage" },
                { "id", (timestamp / 1000).ToString() },
                { "params", new Dictionary<string, object> { { "message", msg } } }
            };

            string jsonBody = JsonConvert.SerializeObject(rpcPayload);

            Debug.Log($"[{playerName}] 正在發送動作: {action}");
            var responseJson = await PostJsonRequest(BASE_URL, jsonBody);

            if (!string.IsNullOrEmpty(responseJson))
            {
                JObject parsed = JObject.Parse(responseJson);
                var taskResult = parsed["result"]?["task"] as JObject;
                return taskResult;
            }

            return null;
        }

        /// <summary>
        /// 模仿 Python SDK 中的 GetTask
        /// </summary>
        public async Task<JObject> GetTaskAsync(string taskId)
        {
            long timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
            var rpcPayload = new Dictionary<string, object>
            {
                { "jsonrpc", "2.0" },
                { "method", "GetTask" },
                { "id", timestamp.ToString() },
                { "params", new Dictionary<string, object> { { "taskId", taskId } } }
            };

            string jsonBody = JsonConvert.SerializeObject(rpcPayload);
            var responseJson = await PostJsonRequest(BASE_URL, jsonBody);

            if (!string.IsNullOrEmpty(responseJson))
            {
                JObject parsed = JObject.Parse(responseJson);
                return parsed["result"]?["task"] as JObject;
            }
            return null;
        }

        /// <summary>
        /// 模仿 Python SDK 的 WaitForTask 輪詢機制
        /// </summary>
        public async Task<JObject> WaitForTaskAsync(string taskId, int timeoutSeconds = 120)
        {
            float startTime = Time.time;
            while (Time.time - startTime < timeoutSeconds)
            {
                JObject taskResult = await GetTaskAsync(taskId);
                if (taskResult != null && taskResult["id"]?.ToString() == taskId)
                {
                    string state = taskResult["status"]?["state"]?.ToString();
                    if (state == "TASK_STATE_COMPLETED" || taskResult["messages"] != null)
                    {
                        return taskResult;
                    }
                }
                
                // 等待 2 秒再次輪詢
                await Task.Delay(2000);
            }

            Debug.LogError("Task polling timeout!");
            return null;
        }

        /// <summary>
        /// 使用 UnityWebRequest 發送非同步 POST 請求
        /// </summary>
        private async Task<string> PostJsonRequest(string url, string json)
        {
            using (UnityWebRequest req = new UnityWebRequest(url, "POST"))
            {
                byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
                req.uploadHandler = new UploadHandlerRaw(bodyRaw);
                req.downloadHandler = new DownloadHandlerBuffer();
                req.SetRequestHeader("Content-Type", "application/json");
                req.SetRequestHeader("User-Agent", "MUD-SDK/1.0 (Unity-Agent)");

                var operation = req.SendWebRequest();

                while (!operation.isDone)
                {
                    await Task.Yield();
                }

                if (req.result == UnityWebRequest.Result.ConnectionError || req.result == UnityWebRequest.Result.ProtocolError)
                {
                    Debug.LogError($"[A2A Error] {req.error}\n{req.downloadHandler.text}");
                    return null;
                }

                return req.downloadHandler.text;
            }
        }
    }
}
*/

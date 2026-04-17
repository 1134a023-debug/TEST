document.addEventListener("DOMContentLoaded", () => {
    // 模擬假資料 (Mock Data)
    const mockStocks = [
        {
            id: '2330',
            name: 'TSMC',
            type: 'Tech',
            price: '920.00',
            change: '+15.00',
            isPositive: true,
            aiComment: '護國神山今天魅力四射！突破前高啦💖',
            avatarConfig: 'seed=Felix&backgroundColor=ffdfbf'
        },
        {
            id: 'AAPL',
            name: 'Apple Inc.',
            type: 'Tech',
            price: '189.20',
            change: '-1.50',
            isPositive: false,
            aiComment: '稍微休息一下也是為了走更長遠的路喔～🍎',
            avatarConfig: 'seed=Avery&backgroundColor=c0aede'
        },
        {
            id: 'NVDA',
            name: 'NVIDIA',
            type: 'Tech/AI',
            price: '1,120.50',
            change: '+45.80',
            isPositive: true,
            aiComment: 'AI 霸主氣場全開！跟著一起嗨起來！🚀✨',
            avatarConfig: 'seed=Liliana&backgroundColor=b6e3f4'
        },
        {
            id: '2881',
            name: '富邦金',
            type: 'Finance',
            price: '73.20',
            change: '+0.40',
            isPositive: true,
            aiComment: '穩穩的也很棒！給踏實的您一個讚👍',
            avatarConfig: 'seed=Mackenzie&backgroundColor=ffd5dc'
        }
    ];

    const container = document.getElementById('bookmark-container');

    const renderCards = () => {
        container.innerHTML = '';
        mockStocks.forEach(stock => {
            const upDownIcon = stock.isPositive ? '<i class="fa-solid fa-caret-up"></i>' : '<i class="fa-solid fa-caret-down"></i>';
            const priceColorClass = stock.isPositive ? 'positive' : 'negative';
            const changeText = `<span class="change ${priceColorClass}" style="font-size:0.9rem">${stock.change} ${upDownIcon}</span>`;
            
            // Dicebear Avatars used as "Idol Portraits" for stocks
            const avatarUrl = `https://api.dicebear.com/9.x/adventurer/svg?${stock.avatarConfig}`;

            const cardHTML = `
                <div class="idol-card">
                    <div class="card-header">
                        <img src="${avatarUrl}" class="card-avatar" alt="${stock.name}">
                    </div>
                    <div class="card-body">
                        <div class="stock-info">
                            <span class="stock-name">${stock.id} ${stock.name}</span>
                        </div>
                        <div class="stock-info">
                            <span class="stock-price">$${stock.price}</span>
                            ${changeText}
                        </div>
                        <div class="stock-tags">
                            <span class="tag idol"><i class="fa-solid fa-star"></i> Pick</span>
                            <span class="tag">${stock.type}</span>
                        </div>
                        <div class="ai-comment">
                            <i class="fa-solid fa-comment-dots" style="color: var(--neon-purple)"></i> ${stock.aiComment}
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += cardHTML;
        });
    };

    renderCards();
});

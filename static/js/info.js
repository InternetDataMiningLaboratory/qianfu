var strategyChart = echarts.init(document.getElementById('Strategy'));
var strategyOption = {
    tooltip: {
        trigger: 'axis',
        formatter: '{b}年<br/>{a1}:{c1}<br />{a0}:{c0}',
        axisPointer: {
            animation: false,
        }
    },
    legend: {
        data:['策略评分', '策略排名'],
        top: '2%',
        right: '2%',
    },
    grid: {
        left: "3%",
        right: "3%",
        bottom: "3%",
        containLabel: true,
    },
    xAxis: {
        type: "category",
              data: $('#Strategy').data('year'),
        boundaryGap: false,
        splitLine: {
            show: false,
        },
        axisLabel: {
            textStyle: {
                fontSize: 14,
            }
        }
    },
    yAxis: [
        {
            type: 'value',
            boundaryGap: [0.2, 0.2],
            axisLabel: {
                textStyle: {
                    fontSize: 14,
                }
            }
        },
        {
            type: 'value',
            inverse: true,
            boundaryGap: [0.2, 0.2],
            axisLabel: {
                textStyle: {
                    fontSize: 14,
                }
            }
        },
    ],
    series: [{
        name: '策略评分',
        type: 'line',
        smooth: 'x',
        data: $('#Strategy').data('score'),
        symbolSize: 10,
        lineStyle: {
            normal: {
                width: 5,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 10,
            }
        }
    },
    {
        name: '策略排名',
        type: 'line',
        smooth: 'x',
        yAxisIndex: 1,
        data: $('#Strategy').data('index'),
        symbolSize: 10,
        lineStyle: {
            normal: {
                width: 5,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 10,
            }
        }
    }
    ]
};
strategyChart.setOption(strategyOption);
$('a[href="#Strategy"]').on('shown.bs.tab', function(e){
    var strategyChart = echarts.init(document.getElementById('Strategy'));
    strategyChart.setOption(strategyOption);
});

var newsOption = {
    textStyle: {
        fontSize: 14,
    },
    tooltip: {
        trigger: 'axis',
        formatter: '{b}年<br/>{a0}:{c0}<br />{a1}:{c1}<br />{a2}:{c2}',
        axisPointer: {
            animation: false,
        }
    },
    legend: {
        data:['总体消息评分', '新闻消息评分', '研报消息评分'],
        top: '2%',
        right: '2%',
    },
    grid: {
        left: "3%",
        right: "3%",
        bottom: "3%",
        containLabel: true,
    },
    xAxis: {
        type: "category",
              data: $('#News').data('year'),
        boundaryGap: false,
        splitLine: {
            show: false,
        },
        axisLabel: {
            textStyle: {
                fontSize: 14,
            }
        }
    },
    yAxis: [
        {
            type: 'value',
            min: 60,
            boundaryGap: [0.2, 0.2],
            axisLabel: {
                textStyle: {
                    fontSize: 14,
                }
            }
        },
    ],
    series: [{
        name: '总体消息评分',
        type: 'line',
        smooth: 'x',
        data: $('#News').data('overall'),
        symbolSize: 10,
        lineStyle: {
            normal: {
                width: 5,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 10,
            }
        }
    },
    {
        name: '新闻消息评分',
        type: 'line',
        smooth: 'x',
        data: $('#News').data('news'),
        symbolSize: 10,
        lineStyle: {
            normal: {
                width: 5,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 10,
            }
        }
    },
    {
        name: '研报消息评分',
        type: 'line',
        smooth: 'x',
        data: $('#News').data('researchreport'),
        symbolSize: 10,
        lineStyle: {
            normal: {
                width: 5,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 10,
            }
        }
    }
    ]
};
$('a[href="#News"]').on('shown.bs.tab', function(e){
    var newsChart = echarts.init(document.getElementById('News'));
    newsChart.setOption(newsOption);
});

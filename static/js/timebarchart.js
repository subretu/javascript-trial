
  async function getTimeData() {
    const res = await fetch('http://127.0.0.1:8000/time');
      const json = await res.json();
      return json
  }

  async function getDayData() {
    const res = await fetch('http://127.0.0.1:8000/day');
      const json = await res.json();
      return json
  }

  async function changeTime() {
    jsondata = await getTimeData();
    create2(jsondata.data, jsondata.label, 'YYYY-MM-DD HH:mm:ss', 'minutes', 100);
  }

  async function changeDay() {
    jsondata = await getDayData();
    create2(jsondata.data, jsondata.label, 'YYYY-MM-DD', 'day', 1);
  }

  function create2(timedata, data_label, timefomat, timeunit, unitsize) {

    var timeOption;
    if(timeunit === 'minutes'){
      timeOption = {
                      parser: 'YYYY-MM-DD HH:mm:ss',
                      unit:  'minutes',
                      stepSize: 100,
                      displayFormats: {
                        'minutes': 'YYYY-MM-DD HH:mm:ss',
                      }
                    }
    }
    else if(timeunit === 'day'){
      timeOption = {
                      parser: 'YYYY-MM-DD',
                      unit:  'day',
                      stepSize: 1,
                      displayFormats: {
                        'day': 'YYYY-MM-DD',
                      }
                    }

    }
    else{
      timeOption = {
                      parser: 'YYYY-MM-DD HH:mm:ss',
                      unit:  'minutes',
                      stepSize: 100,
                      displayFormats: {
                        'minutes': 'YYYY-MM-DD HH:mm:ss',
                      }
                    }
    }

    var ctx = document.getElementById("myChart2");
    var myChart = new Chart(ctx, {
        //線グラフ
        type: 'bar',
        //データ
        data: {
            //各データの時間
            labels: data_label,
            //データセット
            datasets: [{
                label: 'テスト',
                data: timedata,
                backgroundColor: 'red'
            }]
        },
        //グラフ設定
        options: {
            //凡例は非表示
            legend: {
                display: false
            },
            scales: {
                //X軸
                xAxes: [{
                    //軸ラベル表示
                    scaleLabel: {
                        display: false,
                        labelString: '時間'
                    },
                    //ここで軸を時間を設定する
                    type: 'time',
                    time: timeOption,
                    //X軸の範囲を指定
                    ticks: {
                        //min: '2022-03-10 07:00',
                        //max: '2022-03-10 22:00',
                        maxRotation: 90,
                        minRotation: 90,
                    }
                }],
                //Y軸
                yAxes: [{
                    //軸ラベル表示
                    scaleLabel: {
                        display: true,
                    },
                    //Y軸の範囲を指定
                    ticks: {
                        min: 0,
                    }
                }]
            }
        }
    });
  }
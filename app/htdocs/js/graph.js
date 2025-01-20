// Async METHOD to API
async function METHOD(method = 'POST', url = '', data) {
    let payload = {
        method: method,
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: data ? {
            'Content-Type': 'application/json'
        } : {},
        redirect: 'follow',
        referrerPolicy: 'no-referrer'
    }
    if (data) {
        payload.body = JSON.stringify(data);
    }
    try {
        const response = await fetch(url, payload).catch( (e) => {throw e});
        if (response.ok !== true) throw `HTTP Error ${response.status}: ${response.statusText} while fetching [${url}]`
        let js = response.json();
        return js
    } catch (e) {
        alert(e);
    }
}

let GET = (url, data) => METHOD('GET', url, data);

async function graph(element, data) {
  var option;
  const myChart = echarts.init(element)
  myChart.showLoading();
  const webkitDep = await GET(data, '');
  myChart.hideLoading();
  option = {
    legend: {
      data: webkitDep.categories,
      right: 10,
      top: 20,
      bottom: 20
    },
    series: [
      {
        type: 'graph',
        layout: 'force',
      label: {
        position: 'right',
        formatter: '{b}'
      },
        edgeSymbol: ['circle', 'arrow'],
        categories: webkitDep.categoryObjects,
        data: webkitDep.nodes.map(function (node, idx) {
          node.id = idx;
          return node;
        }),
      draggable: true,
        edges: webkitDep.links,
        force: {
          edgeLength: 15,
          repulsion: 20,
          gravity: 0.2
        },
      }
    ]
  };
  //myChart.on('click', function(params) {
  //  alert(params.name);
  //});
  myChart.setOption(option);
}

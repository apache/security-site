// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

(function () {
  "use strict";

  var el = document.getElementById("debt-chart");
  var status = document.getElementById("debt-chart-status");
  if (!el) {
    return;
  }
  if (typeof echarts === "undefined") {
    if (status) {
      status.textContent =
        "ECharts library not found. Add it at /assets/js/echarts.min.js.";
    }
    return;
  }

  var chart = echarts.init(el);
  chart.showLoading();

  const match = window.location.pathname.match(/^\/project\/([^/]+)/);
  const pmc = match ? `?pmc=${match[1]}` : "";

  fetch("/api/statistics/debt" + pmc, { headers: { Accept: "application/json" } })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("HTTP " + response.status);
      }
      return response.json();
    })
    .then(function (data) {
      chart.hideLoading();

      if (!data.series || data.series.length === 0) {
        if (status) {
          status.textContent = "No project debt to display.";
        }
        return;
      }

      var series = data.series.map(function (s) {
        return {
          name: s.name,
          type: "line",
          showSymbol: false,
          emphasis: { focus: "series" },
          data: s.values,
        };
      });

      chart.setOption({
        tooltip: {
          trigger: "axis",
          confine: true,
          appendToBody: true,
          enterable: true,
          extraCssText: "max-height: 80vh; overflow-y: auto;",
          formatter: function (params) {
            var rows = params
              .filter(function (p) {
                return p.value;
              })
              .sort(function (a, b) {
                return b.value - a.value;
              });
            if (rows.length === 0) {
              return "";
            }
            var html = rows[0].axisValueLabel;
            rows.forEach(function (p) {
              html +=
                "<br/>" + p.marker + p.seriesName + ": <b>" + p.value + "</b>";
            });
            return html;
          },
        },
        legend: { type: "scroll", top: 0 },
        grid: { left: 64, right: 24, top: 56, bottom: 80, containLabel: true },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: data.weeks,
          name: "week ending",
        },
        yAxis: { type: "value", name: "project debt" },
        dataZoom: [{ type: "inside" }, { type: "slider" }],
        series: series,
      });
    })
    .catch(function (err) {
      chart.hideLoading();
      if (status) {
        status.textContent = "Failed to load debt data: " + err.message;
      }
    });

  window.addEventListener("resize", function () {
    chart.resize();
  });
})();

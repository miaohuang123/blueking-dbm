# 添加tags

"tags": ["{cluster_type}"]
___________________________________
"tags": ["es"],
"tags": ["hdfs"],
"tags": ["kafka"],
"tags": ["pulsar"],
"tags": ["tendbha"],
"tags": ["tendbsingle"],
"tags": ["tendbha"],
"tags": ["TwemproxyRedisInstance"],
"tags": ["PredixyTendisplusCluster"],
"tags": ["TwemproxyTendisSSDInstance"],

# 刷新监控数据源ID：bkmonitor_timeseries
cd backend/bk_dataview/dashboards/json
find . -type f -name "*.json" -exec sed -i '' -e 's#${DS_蓝鲸监控_- 指标数据}#bkmonitor_timeseries#g' {} \;
find . -type f -name "*.json" -exec sed -i '' -e 's#"editable": true#"editable": false#g' {} \;

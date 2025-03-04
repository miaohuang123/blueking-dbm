# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-DB管理系统(BlueKing-BK-DBM) available.
Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from blue_krill.data_types.enum import EnumField, StructuredEnum
from django.utils.translation import ugettext_lazy as _

from backend.db_meta.enums import ClusterType
from backend.db_meta.enums.cluster_phase import ClusterPhase
from backend.db_meta.exceptions import ClusterExclusiveOperateException
from backend.flow.consts import StateType


class InstanceType(str, StructuredEnum):
    STORAGE = EnumField("storage", _("storage"))
    PROXY = EnumField("proxy", _("proxy"))


class TodoType(str, StructuredEnum):
    """
    待办类型
    """

    APPROVE = EnumField("APPROVE", _("主流程-人工确认"))
    INNER_APPROVE = EnumField("INNER_APPROVE", _("自动化流程-人工确认"))


class CountType(str, StructuredEnum):
    """
    单据计数类型
    """

    MY_TODO = EnumField("MY_TODO", _("我的待办"))
    MY_APPROVE = EnumField("MY_APPROVE", _("我的申请"))


class TodoStatus(str, StructuredEnum):
    """
    待办状态枚举
       TODO -> (RUNNING，可选) -> DONE_SUCCESS
                            | -> DONE_FAILED
    """

    TODO = EnumField("TODO", _("待处理"))
    RUNNING = EnumField("RUNNING", _("处理中"))
    DONE_SUCCESS = EnumField("DONE_SUCCESS", _("已处理"))
    DONE_FAILED = EnumField("DONE_FAILED", _("已终止"))


DONE_STATUS = [TodoStatus.DONE_SUCCESS, TodoStatus.DONE_FAILED]


class TicketStatus(str, StructuredEnum):
    """单据状态枚举"""

    PENDING = EnumField("PENDING", _("等待中"))
    RUNNING = EnumField("RUNNING", _("执行中"))
    SUCCEEDED = EnumField("SUCCEEDED", _("成功"))
    FAILED = EnumField("FAILED", _("失败"))
    REVOKED = EnumField("REVOKED", _("撤销"))


class TicketFlowStatus(str, StructuredEnum):
    """单据流程状态枚举类"""

    PENDING = EnumField("PENDING", _("等待中"))
    RUNNING = EnumField("RUNNING", _("执行中"))
    SUCCEEDED = EnumField("SUCCEEDED", _("成功"))
    FAILED = EnumField("FAILED", _("失败"))
    REVOKED = EnumField("REVOKED", _("撤销"))
    SKIPPED = EnumField("SKIPPED", _("跳过"))


FLOW_FINISHED_STATUS = [TicketFlowStatus.SKIPPED, TicketStatus.SUCCEEDED]
FLOW_NOT_EXECUTE_STATUS = [TicketFlowStatus.SKIPPED, TicketStatus.PENDING]

BAMBOO_STATE__TICKET_STATE_MAP = {
    StateType.FINISHED.value: TicketFlowStatus.SUCCEEDED.value,
    StateType.FAILED.value: TicketFlowStatus.FAILED.value,
    StateType.REVOKED.value: TicketFlowStatus.REVOKED.value,
}

EXCLUSIVE_TICKET_EXCEL_PATH = "backend/ticket/exclusive_ticket.xlsx"


class TicketType(str, StructuredEnum):
    """单据类型枚举"""

    @classmethod
    def get_choice_value(cls, label: str) -> str:
        """Get the value of field member by label"""

        members = cls.get_field_members()
        for field in members.values():
            if label in field.label:
                return field.real_value

        return label

    # MYSQL
    MYSQL_SINGLE_APPLY = EnumField("MYSQL_SINGLE_APPLY", _("MySQL 单节点部署"))
    MYSQL_ADD_SLAVE = EnumField("MYSQL_ADD_SLAVE", _("MySQL 添加从库"))
    MYSQL_RESTORE_SLAVE = EnumField("MYSQL_RESTORE_SLAVE", _("MySQL Slave重建"))
    MYSQL_RESTORE_LOCAL_SLAVE = EnumField("MYSQL_RESTORE_LOCAL_SLAVE", _("MySQL Slave原地重建"))
    MYSQL_MIGRATE_CLUSTER = EnumField("MYSQL_MIGRATE_CLUSTER", _("MySQL 克隆主从"))
    MYSQL_MASTER_SLAVE_SWITCH = EnumField("MYSQL_MASTER_SLAVE_SWITCH", _("MySQL 主从互换"))
    MYSQL_MASTER_FAIL_OVER = EnumField("MYSQL_MASTER_FAIL_OVER", _("MySQL 主库故障切换"))
    MYSQL_HA_APPLY = EnumField("MYSQL_HA_APPLY", _("MySQL 高可用部署"))
    MYSQL_IMPORT_SQLFILE = EnumField("MYSQL_IMPORT_SQLFILE", _("MySQL 变更SQL执行"))
    MYSQL_SEMANTIC_CHECK = EnumField("MYSQL_SEMANTIC_CHECK", _("MySQL 模拟执行"))
    MYSQL_PROXY_ADD = EnumField("MYSQL_PROXY_ADD", _("MySQL 添加Proxy"))
    MYSQL_PROXY_SWITCH = EnumField("MYSQL_PROXY_SWITCH", _("MySQL 替换Proxy"))
    MYSQL_SINGLE_DESTROY = EnumField("MYSQL_SINGLE_DESTROY", _("MySQL 单节点删除"))
    MYSQL_SINGLE_ENABLE = EnumField("MYSQL_SINGLE_ENABLE", _("MySQL 单节点启用"))
    MYSQL_SINGLE_DISABLE = EnumField("MYSQL_SINGLE_DISABLE", _("MySQL 单节点禁用"))
    MYSQL_HA_DESTROY = EnumField("MYSQL_HA_DESTROY", _("MySQL 高可用删除"))
    MYSQL_HA_DISABLE = EnumField("MYSQL_HA_DISABLE", _("MySQL 高可用禁用"))
    MYSQL_HA_ENABLE = EnumField("MYSQL_HA_ENABLE", _("MySQL 高可用启用"))
    MYSQL_AUTHORIZE_RULES = EnumField("MYSQL_AUTHORIZE_RULES", _("MySQL 授权"))
    MYSQL_EXCEL_AUTHORIZE_RULES = EnumField("MYSQL_EXCEL_AUTHORIZE_RULES", _("MySQL EXCEL-授权"))
    MYSQL_CLIENT_CLONE_RULES = EnumField("MYSQL_CLIENT_CLONE_RULES", _("MySQL 客户端权限克隆"))
    MYSQL_INSTANCE_CLONE_RULES = EnumField("MYSQL_INSTANCE_CLONE_RULES", _("MySQL DB实例权限克隆"))
    MYSQL_HA_RENAME_DATABASE = EnumField("MYSQL_HA_RENAME_DATABASE", _("MySQL 高可用DB重命名"))
    MYSQL_HA_TRUNCATE_DATA = EnumField("MYSQL_HA_TRUNCATE_DATA", _("MySQL 高可用清档"))
    MYSQL_HA_DB_TABLE_BACKUP = EnumField("MYSQL_HA_DB_TABLE_BACKUP", _("MySQL 高可用库表备份"))
    MYSQL_CHECKSUM = EnumField("MYSQL_CHECKSUM", _("MySQL 数据校验修复"))
    MYSQL_PARTITION = EnumField("MYSQL_PARTITION", _("MySQL 分区"))
    MYSQL_DATA_REPAIR = EnumField("MYSQL_DATA_REPAIR", _("MySQL 数据修复"))
    MYSQL_FLASHBACK = EnumField("MYSQL_FLASHBACK", _("MySQL 闪回"))
    MYSQL_ROLLBACK_CLUSTER = EnumField("MYSQL_ROLLBACK_CLUSTER", _("MySQL 定点回档"))
    MYSQL_HA_FULL_BACKUP = EnumField("MYSQL_HA_FULL_BACKUP", _("MySQL 高可用全库备份"))
    MYSQL_SINGLE_TRUNCATE_DATA = EnumField("MYSQL_SINGLE_TRUNCATE_DATA", _("MySQL 单节点清档"))
    MYSQL_SINGLE_RENAME_DATABASE = EnumField("MYSQL_SINGLE_RENAME_DATABASE", _("MySQL 单节点DB重命名"))

    # SPIDER
    SPIDER_CHECKSUM = EnumField("SPIDER_CHECKSUM", _("Spider 数据校验修复"))
    SPIDER_PARTITION = EnumField("SPIDER_PARTITION", _("Spider 分区管理"))
    SPIDER_DB_TABLE_BACKUP = EnumField("SPIDER_DB_TABLE_BACKUP", _("Spider 库表备份"))
    SPIDER_RENAME_DATABASE = EnumField("SPIDER_RENAME_DATABASE", _("Spider 数据库重命名"))
    SPIDER_TRUNCATE_DATABASE = EnumField("SPIDER_TRUNCATE_DATABASE", _("Spider 清档"))
    # SPIDER(TenDB Cluster)
    SPIDER_MASTER_FAIL_OVER = EnumField("SPIDER_MASTER_FAIL_OVER", _("TenDB Cluster 主故障切换"))
    SPIDER_MASTER_SLAVE_SWITCH = EnumField("SPIDER_MASTER_SLAVE_SWITCH", _("TenDB Cluster 主从互切"))
    TENDB_CLUSTER_APPLY = EnumField("TENDB_CLUSTER_APPLY", _("TenDB Cluster 集群部署"))
    TENDB_CLUSTER_ENABLE = EnumField("TENDB_CLUSTER_ENABLE", _("TenDB Cluster 集群启用"))
    TENDB_CLUSTER_DISABLE = EnumField("TENDB_CLUSTER_DISABLE", _("TenDB Cluster 集群禁用"))
    TENDB_CLUSTER_DESTROY = EnumField("TENDB_CLUSTER_DESTROY", _("TenDB Cluster 集群销毁"))

    # REDIS
    REDIS_SINGLE_APPLY = EnumField("REDIS_SINGLE_APPLY", _("Redis 单节点部署"))
    REDIS_CLUSTER_APPLY = EnumField("REDIS_CLUSTER_APPLY", _("Redis 集群部署"))
    REDIS_KEYS_EXTRACT = EnumField("REDIS_KEYS_EXTRACT", _("Redis 提取 Key"))
    REDIS_KEYS_DELETE = EnumField("REDIS_KEYS_DELETE", _("Redis 删除 key"))
    REDIS_BACKUP = EnumField("REDIS_BACKUP", _("Redis 集群备份"))
    REDIS_OPEN = EnumField("REDIS_PROXY_OPEN", _("Redis 集群启用"))
    REDIS_CLOSE = EnumField("REDIS_PROXY_CLOSE", _("Redis 集群禁用"))
    REDIS_DESTROY = EnumField("REDIS_DESTROY", _("Redis 集群删除"))
    REDIS_PURGE = EnumField("REDIS_PURGE", _("Redis 集群清档"))
    REDIS_SCALE = EnumField("REDIS_SCALE", _("Redis 扩缩容"))
    PROXY_SCALE = EnumField("PROXY_SCALE", _("Proxy 扩缩容"))
    REDIS_CLUSTER_SLAVE_CUTOFF = EnumField("REDIS_CLUSTER_SLAVE_CUTOFF", _("redis集群 slave 裁撤替换"))
    REDIS_CLUSTER_MASTER_CUTOFF = EnumField("REDIS_CLUSTER_MASTER_CUTOFF", _("redis集群 master 裁撤替换"))
    REDIS_CLUSTER_PROXY_CUTOFF = EnumField("REDIS_CLUSTER_PROXY_CUTOFF", _("redis集群 proxy 裁撤替换"))
    REDIS_NEW_DTS_JOB = EnumField("REDIS_NEW_DTS_JOB", _("Redis 新建DTS任务"))

    # 大数据
    KAFKA_APPLY = EnumField("KAFKA_APPLY", _("Kafka 集群部署"))
    KAFKA_SCALE_UP = EnumField("KAFKA_SCALE_UP", _("Kafka 集群扩容"))
    KAFKA_SHRINK = EnumField("KAFKA_SHRINK", _("Kafka 集群缩容"))
    KAFKA_REBOOT = EnumField("KAFKA_REBOOT", _("Kafka 实例重启"))
    KAFKA_REPLACE = EnumField("KAFKA_REPLACE", _("Kafka 集群替换"))
    KAFKA_ENABLE = EnumField("KAFKA_ENABLE", _("Kafka 集群启用"))
    KAFKA_DISABLE = EnumField("KAFKA_DISABLE", _("Kafka 集群禁用"))
    KAFKA_DESTROY = EnumField("KAFKA_DESTROY", _("Kafka 集群删除"))

    HDFS_APPLY = EnumField("HDFS_APPLY", _("HDFS 集群部署"))
    HDFS_SCALE_UP = EnumField("HDFS_SCALE_UP", _("HDFS 集群扩容"))
    HDFS_SHRINK = EnumField("HDFS_SHRINK", _("HDFS 集群缩容"))
    HDFS_REBOOT = EnumField("HDFS_REBOOT", _("HDFS 实例重启"))
    HDFS_REPLACE = EnumField("HDFS_REPLACE", _("HDFS 集群替换"))
    HDFS_ENABLE = EnumField("HDFS_ENABLE", _("HDFS 集群启用"))
    HDFS_DISABLE = EnumField("HDFS_DISABLE", _("HDFS 集群禁用"))
    HDFS_DESTROY = EnumField("HDFS_DESTROY", _("HDFS 集群删除"))

    ES_APPLY = EnumField("ES_APPLY", _("ES 集群部署"))
    ES_SCALE_UP = EnumField("ES_SCALE_UP", _("ES 集群扩容"))
    ES_SHRINK = EnumField("ES_SHRINK", _("ES 集群缩容"))
    ES_REBOOT = EnumField("ES_REBOOT", _("ES 实例重启"))
    ES_REPLACE = EnumField("ES_REPLACE", _("ES 集群替换"))
    ES_ENABLE = EnumField("ES_ENABLE", _("ES 集群启用"))
    ES_DISABLE = EnumField("ES_DISABLE", _("ES 集群禁用"))
    ES_DESTROY = EnumField("ES_DESTROY", _("ES 集群删除"))

    PULSAR_APPLY = EnumField("PULSAR_APPLY", _("PULSAR 集群部署"))
    PULSAR_SCALE_UP = EnumField("PULSAR_SCALE_UP", _("PULSAR 集群扩容"))
    PULSAR_SHRINK = EnumField("PULSAR_SHRINK", _("PULSAR 集群缩容"))
    PULSAR_REBOOT = EnumField("PULSAR_REBOOT", _("PULSAR 实例重启"))
    PULSAR_REPLACE = EnumField("PULSAR_REPLACE", _("PULSAR 集群替换"))
    PULSAR_ENABLE = EnumField("PULSAR_ENABLE", _("PULSAR 集群启用"))
    PULSAR_DISABLE = EnumField("PULSAR_DISABLE", _("PULSAR 集群禁用"))
    PULSAR_DESTROY = EnumField("PULSAR_DESTROY", _("PULSAR 集群删除"))

    INFLUXDB_APPLY = EnumField("INFLUXDB_APPLY", _("InfluxDB 实例部署"))
    INFLUXDB_REBOOT = EnumField("INFLUXDB_REBOOT", _("InfluxDB 实例重启"))
    INFLUXDB_ENABLE = EnumField("INFLUXDB_ENABLE", _("InfluxDB 实例启用"))
    INFLUXDB_DISABLE = EnumField("INFLUXDB_DISABLE", _("InfluxDB 实例禁用"))
    INFLUXDB_DESTROY = EnumField("INFLUXDB_DESTROY", _("InfluxDB 实例删除"))
    INFLUXDB_REPLACE = EnumField("INFLUXDB_REPLACE", _("InfluxDB 实例替换"))

    # 云区域组件
    CLOUD_SERVICE_APPLY = EnumField("CLOUD_SERVICE_APPLY", _("云区域服务部署"))
    CLOUD_NGINX_APPLY = EnumField("CLOUD_NGINX_APPLY", _("云区域Nginx 服务部署"))
    CLOUD_NGINX_RELOAD = EnumField("CLOUD_NGINX_RELOAD", _("云区域nginx 服务重装"))
    CLOUD_NGINX_REPLACE = EnumField("CLOUD_NGINX_REPLACE", _("云区域nginx 服务替换"))
    CLOUD_DNS_APPLY = EnumField("CLOUD_DNS_APPLY", _("云区域dns 服务部署"))
    CLOUD_DNS_ADD = EnumField("CLOUD_DNS_ADD", _("云区域dns 服务添加"))
    CLOUD_DNS_REDUCE = EnumField("CLOUD_DNS_REDUCE", _("云区域dns 服务裁撤"))
    CLOUD_DNS_REPLACE = EnumField("CLOUD_DNS_REPLACE", _("云区域dns 服务替换"))
    CLOUD_DNS_RELOAD = EnumField("CLOUD_DNS_RELOAD", _("云区域dns 服务重装"))
    CLOUD_DBHA_APPLY = EnumField("CLOUD_DBHA_APPLY", _("云区域dbha 服务部署"))
    CLOUD_DBHA_RELOAD = EnumField("CLOUD_DBHA_RELOAD", _("云区域dbha 服务重装"))
    CLOUD_DBHA_REPLACE = EnumField("CLOUD_DBHA_REPLACE", _("云区域dbha 服务替换"))
    CLOUD_DBHA_ADD = EnumField("CLOUD_DBHA_ADD", _("云区域dbha 服务新增"))
    CLOUD_DBHA_REDUCE = EnumField("CLOUD_DBHA_REDUCE", _("云区域dbha 服务删除"))
    CLOUD_DRS_APPLY = EnumField("CLOUD_DRS_APPLY", _("云区域drs 服务部署"))
    CLOUD_DRS_RELOAD = EnumField("CLOUD_DRS_RELOAD", _("云区域drs 服务重启"))
    CLOUD_DRS_ADD = EnumField("CLOUD_DRS_ADD", _("云区域drs 服务新增"))
    CLOUD_DRS_REDUCE = EnumField("CLOUD_DRS_REDUCE", _("云区域drs 服务删除"))
    CLOUD_DRS_REPLACE = EnumField("CLOUD_DRS_REPLACE", _("云区域drs 服务替换"))

    # 资源池
    RESOURCE_IMPORT = EnumField("RESOURCE_IMPORT", _("资源池导入"))


# 单据动作与集群状态的映射
TICKET_TYPE__CLUSTER_PHASE_MAP = {
    # MySQL单据----MySQL phase
    TicketType.MYSQL_HA_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.MYSQL_HA_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.MYSQL_HA_DESTROY.value: ClusterPhase.DESTROY.value,
    TicketType.MYSQL_SINGLE_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.MYSQL_SINGLE_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.MYSQL_SINGLE_DESTROY.value: ClusterPhase.DESTROY.value,
    # ES单据---ES phase
    TicketType.ES_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.ES_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.ES_DESTROY.value: ClusterPhase.DESTROY.value,
    # Kafka单据---Kafka phase
    TicketType.KAFKA_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.KAFKA_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.KAFKA_DESTROY.value: ClusterPhase.DESTROY.value,
    # Hdfs单据---Hdfs phase
    TicketType.HDFS_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.HDFS_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.HDFS_DESTROY.value: ClusterPhase.DESTROY.value,
    # Pulsar单据---Pulsar phase
    TicketType.PULSAR_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.PULSAR_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.PULSAR_DESTROY.value: ClusterPhase.DESTROY.value,
    # Influxdb单据---Influxdb phase
    TicketType.INFLUXDB_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.INFLUXDB_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.INFLUXDB_DESTROY.value: ClusterPhase.DESTROY.value,
    # Spider单据---Spider phase
    TicketType.TENDB_CLUSTER_ENABLE.value: ClusterPhase.ONLINE.value,
    TicketType.TENDB_CLUSTER_DISABLE.value: ClusterPhase.OFFLINE.value,
    TicketType.TENDB_CLUSTER_DESTROY.value: ClusterPhase.DESTROY.value,
}

# 单据类型和集群类型的映射
TICKET_TYPE__CLUSTER_TYPE_MAP = {
    # MySQL
    TicketType.MYSQL_SINGLE_APPLY: ClusterType.TenDBSingle,
    TicketType.MYSQL_HA_APPLY: ClusterType.TenDBHA,
    # 大数据
    TicketType.KAFKA_APPLY: ClusterType.Kafka,
    TicketType.HDFS_APPLY: ClusterType.Hdfs,
    TicketType.ES_APPLY: ClusterType.Es,
    TicketType.PULSAR_APPLY: ClusterType.Pulsar,
    TicketType.INFLUXDB_APPLY: ClusterType.Influxdb
    # Redis TODO: redis集群类型太多了，但是单据类型就一种，如何区分？
}

# 扩容单据合集
SCALE_UP_TICKET_TYPES = [
    TicketType.REDIS_SCALE,
    TicketType.ES_SCALE_UP,
    TicketType.HDFS_SCALE_UP,
    TicketType.KAFKA_SCALE_UP,
    TicketType.PULSAR_SCALE_UP,
    TicketType.PROXY_SCALE,
]


class FlowType(str, StructuredEnum):
    """流程类型枚举"""

    # 蓝鲸ITSM流程服务
    BK_ITSM = EnumField("BK_ITSM", _("单据审批"))
    # 内建执行流程
    INNER_FLOW = EnumField("INNER_FLOW", _("生产部署"))
    # 内建快速执行流程
    QUICK_INNER_FLOW = EnumField("QUICK_INNER_FLOW", _("快速执行"))
    # 内建结果忽略执行流程
    IGNORE_RESULT_INNER_FLOW = EnumField("IGNORE_RESULT_INNER_FLOW", _("结果忽略执行"))
    # 暂停节点
    PAUSE = EnumField("PAUSE", _("暂停"))
    # 交付节点，仅作为流程结束的标志
    DELIVERY = EnumField("DELIVERY", _("交付"))
    # 描述节点，描述触发创建该单据的任务信息
    DESCRIBE_TASK = EnumField("DESCRIBE_TASK", _("描述任务信息"))
    # 定时节点，用于定时触发单据流程的下一个节点
    TIMER = EnumField("TIMER", _("定时"))
    # 资源申请节点，用于根据资源规格申请对应机器
    RESOURCE_APPLY = EnumField("RESOURCE_APPLY", _("资源申请"))
    # 资源交付节点，用于机器部署成功后通过资源池服务
    RESOURCE_DELIVERY = EnumField("RESOURCE_DELIVERY", _("资源交付"))
    # 资源批量申请节点
    RESOURCE_BATCH_APPLY = EnumField("RESOURCE_BATCH_APPLY", _("资源批量申请"))
    # 资源批量交付节点
    RESOURCE_BATCH_DELIVERY = EnumField("RESOURCE_BATCH_DELIVERY", _("资源批量交付"))


class FlowCallbackType(str, StructuredEnum):
    """flow钩子工作类型"""

    PRE_CALLBACK = EnumField("pre", _("前置动作"))
    POST_CALLBACK = EnumField("post", _("后继动作"))


class FlowRetryType(str, StructuredEnum):
    """inner flow的重试类型(目前用于互斥执行)"""

    AUTO_RETRY = EnumField("auto_retry", _("自动重试"))
    MANUAL_RETRY = EnumField("manual_retry", _("手动重试"))


class FlowErrCode(int, StructuredEnum):
    """flow的错误代码"""

    GENERAL_ERROR = EnumField(0, _("通用错误代码"))
    AUTO_EXCLUSIVE_ERROR = EnumField(1, _("自动互斥重试错误代码"))
    MANUAL_EXCLUSIVE_ERROR = EnumField(2, _("手动互斥重试错误代码"))

    @classmethod
    def get_err_code(cls, err: Exception, retry_type: str) -> "FlowErrCode":
        # 不是互斥错误，统一认为是其他通用错误
        if not isinstance(err, ClusterExclusiveOperateException):
            return cls.GENERAL_ERROR

        err_code = cls.MANUAL_EXCLUSIVE_ERROR if retry_type == FlowRetryType.MANUAL_RETRY else cls.AUTO_EXCLUSIVE_ERROR
        return err_code

/*
 * TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-DB管理系统(BlueKing-BK-DBM) available.
 *
 * Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
 *
 * Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at https://opensource.org/licenses/MIT
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
 * the specific language governing permissions and limitations under the License.
*/

import { acceptHMRUpdate, defineStore } from 'pinia';

import { getRelatedSystemUrls } from '@services/common';

interface Urls {
  [key: string]: string
}
/**
 * 获取关联系统 url
 */
export const useRelatedSystem = defineStore('RelatedSystem', {
  state: (): { urls: Urls } => ({
    urls: {},
  }),
  actions: {
    /**
     * 获取关联系统 urls
     */
    fetchRelatedSystemUrls() {
      getRelatedSystemUrls().then((res) => {
        this.urls = res;
      });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useRelatedSystem, import.meta.hot));
}

<template>
  <div class="contaienr">
    <div class="form-warpper">
      <div class="about">
        <img :src="info.picture_url" alt>
      </div>
      <el-button type="primary" @click="updateVisible = true">修改</el-button>
    </div>
    <!-- 修改弹窗 -->
    <update-info :data-source="info" :visible.sync="updateVisible" @success="queryAbout" />
  </div>
</template>

<script>
import UpdateInfo from './components/UpdateInfo'
import * as Api from '@/api'
export default {
  name: 'About',
  components: {
    UpdateInfo
  },
  data() {
    return {
      updateVisible: false,
      info: {}
    }
  },
  mounted() {
    this.queryAbout()
  },
  methods: {
    /**
     * 修改信息
     */
    handleUpdate(row) {
      this.updateVisible = true
      this.updateRow = row
    },
    /**
     * 获取数据
     */
    queryAbout() {
      const params = { page_size: 1, page_number: 1 }
      Api.queryAbout(params).then(res => {
        if (res && res.code === '200') {
          this.info = res.data
        } else {
          this.$message.error('查询列表失败！')
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.contaienr {
  min-width: 1000px;
  padding: 20px;
  .form-warpper {
    margin-bottom: 20px;
    padding: 10px 20px;
    background-color: #fff;
  }
  .about {
    margin-top: 20px;
    img {
      width: 240px;
      height: 360px;
    }
  }
}
</style>

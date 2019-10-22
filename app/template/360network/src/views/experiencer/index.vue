<template>
  <div class="contaienr">
    <my-table
      v-loading="isLoading"
      :data-source="tableData"
      :total-num="totalNum"
      :page-size="pageSize"
      :cur-page="pageNum"
      @page-change="handlePageChange"
    />
  </div>
</template>

<script>
import MyTable from './components/MyTable'
import * as Api from '@/api'
export default {
  name: '',
  components: {
    MyTable
  },
  data() {
    return {
      isLoading: true,
      tableData: [],
      totalNum: 0,
      pageSize: 15,
      pageNum: 1
    }
  },
  mounted() {
    this.queryExperiencer()
  },
  methods: {
    /**
     * 表格分页
     */
    handlePageChange(page) {
      this.pageNum = page
      this.queryExperiencer()
    },
    /**
     * 获取表格数据
     */
    queryExperiencer() {
      const params = { page_size: this.pageSize, page_number: this.pageNum }
      this.isLoading = true
      Api.queryExperiencer(params).then(res => {
        this.isLoading = false
        if (res && res.code === '200') {
          const result = res.data
          this.tableData = result.list
          this.totalNum = result.total
        } else {
          this.$message.error('查询失败！')
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
}
</style>

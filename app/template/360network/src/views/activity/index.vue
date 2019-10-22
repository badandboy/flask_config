<template>
  <div class="contaienr">
    <div class="form-warpper">
      <el-button type="primary" @click="addVisible = true">新增活动信息</el-button>
    </div>
    <my-table
      v-loading="isLoading"
      :data-source="tableData"
      :total-num="totalNum"
      :page-size="pageSize"
      :cur-page="pageNum"
      @page-change="handlePageChange"
      @update-row="handleUpdate"
      @delete-row="handleDelete"
    />
    <!-- 新增弹窗 -->
    <add-info :visible.sync="addVisible" @success="queryActivity" />
    <!-- 修改弹窗 -->
    <update-info :data-source="updateRow" :visible.sync="updateVisible" @success="queryActivity" />
  </div>
</template>

<script>
import MyTable from './components/MyTable'
import AddInfo from './components/AddInfo'
import UpdateInfo from './components/UpdateInfo'
import * as Api from '@/api'
export default {
  name: '',
  components: {
    MyTable,
    AddInfo,
    UpdateInfo
  },
  data() {
    return {
      isLoading: false,
      addVisible: false,
      updateVisible: false,
      tableData: [],
      totalNum: 0,
      pageSize: 15,
      pageNum: 1,
      updateRow: {}
    }
  },
  mounted() {
    this.queryActivity()
  },
  methods: {
    /**
     * 删除信息
     */
    handleDelete(row) {
      this.$confirm('确定永久删除该条信息?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          Api.deleteActivity({
            activity_id: row.activity_id
          }).then(res => {
            if (res && res.code === '200') {
              this.$message({
                type: 'success',
                message: '删除成功!'
              })
              this.queryActivity()
            }
          })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
    },
    /**
     * 修改信息
     */
    handleUpdate(row) {
      this.updateVisible = true
      this.updateRow = row
    },
    /**
     * 表格分页
     */
    handlePageChange(page) {
      this.pageNum = page
      this.queryActivity()
    },
    /**
     * 获取表格数据
     */
    queryActivity() {
      const params = { page_size: this.pageSize, page_number: this.pageNum }
      this.isLoading = true
      Api.queryActivity(params).then(res => {
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

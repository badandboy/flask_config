<template>
  <div class="contaienr">
    <div class="form-warpper">
      <el-button type="primary" @click="addVisible = true">新增课程</el-button>
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
    <add-info :visible.sync="addVisible" @success="queryCourse" />
    <!-- 修改弹窗 -->
    <update-info :data-source="updateRow" :visible.sync="updateVisible" @success="queryCourse" />
  </div>
</template>

<script>
import MyTable from './components/MyTable'
import AddInfo from './components/AddInfo'
import UpdateInfo from './components/UpdateInfo'
import * as Api from '@/api'
export default {
  name: 'Course',
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
    this.queryCourse()
  },
  methods: {
    /**
     * 删除信息
     */
    handleDelete(row) {
      this.$confirm('确定永久删除该课程?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          Api.deleteCourse({
            course_id: row.course_id
          }).then(res => {
            if (res && res.code === '200') {
              this.$message({
                type: 'success',
                message: '删除成功!'
              })
              this.queryCourse()
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
      this.queryCourse()
    },
    /**
     * 获取表格数据
     */
    queryCourse() {
      const params = { page_size: this.pageSize, page_number: this.pageNum }
      this.isLoading = true
      Api.queryCourse(params).then(res => {
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

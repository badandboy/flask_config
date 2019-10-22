<template>
  <div class="contaienr">
    <div class="form-warpper">
      <el-button type="primary" @click="addVisible = true">新增教师</el-button>
    </div>
    <teacher-table
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
    <add-teacher-info :visible.sync="addVisible" @success="queryTeacher" />
    <!-- 修改弹窗 -->
    <update-teacher-info
      :data-source="updateRow"
      :visible.sync="updateVisible"
      @success="queryTeacher"
    />
  </div>
</template>

<script>
import TeacherTable from './components/TeacherTable'
import AddTeacherInfo from './components/AddTeacherInfo'
import UpdateTeacherInfo from './components/UpdateTeacherInfo'
import * as Api from '@/api'
export default {
  name: 'Teacher',
  components: {
    TeacherTable,
    AddTeacherInfo,
    UpdateTeacherInfo
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
    this.queryTeacher()
  },
  methods: {
    /**
     * 删除信息
     */
    handleDelete(row) {
      this.$confirm('确定永久删除该信息?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          Api.deleteTeacher({
            teacher_id: row.teacher_id
          }).then(res => {
            if (res && res.code === '200') {
              this.$message({
                type: 'success',
                message: '删除成功!'
              })
              this.queryTeacher()
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
      this.queryTeacher()
    },
    /**
     * 获取表格数据
     */
    queryTeacher() {
      const params = { page_size: this.pageSize, page_number: this.pageNum }
      this.isLoading = true
      Api.queryTeacher(params).then(res => {
        this.isLoading = false
        if (res && res.code === '200') {
          const result = res.data
          this.tableData = result.list
          this.totalNum = result.total
        } else {
          this.$message.error('查询师资失败！')
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

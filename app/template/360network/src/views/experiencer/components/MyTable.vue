<template>
  <div>
    <el-table :data="dataSource" style="width: 100%">
      <el-table-column type="index" width="50" />
      <el-table-column prop="name" label="姓名" width="180" />
      <el-table-column prop="telephone_number" label="电话" width="180" />
      <el-table-column prop="industry" label="行业" />
      <el-table-column prop="company" label="公司" />
      <el-table-column prop="industry" label="职位" />
      <el-table-column prop="course_choose" label="课程选择" />
      <el-table-column prop="created_at" label="时间" width="180" />
    </el-table>
    <el-pagination
      background
      class="pagination"
      layout="prev, pager, next"
      :page-size="pageSize"
      :current-page.sync="pageNum"
      :total="totalNum"
      @current-change="pageChange"
      @prev-click="pageChange"
      @next-click="pageChange"
    />
  </div>
</template>

<script>
export default {
  props: {
    dataSource: {
      type: Array,
      default: function() {
        return []
      }
    },
    isLoading: {
      type: Boolean,
      default: function() {
        return false
      }
    },
    totalNum: [String, Number],
    pageSize: [String, Number],
    curPage: [String, Number]
  },
  data() {
    return {
      pageNum: 1
    }
  },
  watch: {
    curPage: function(val) {
      this.pageNum = val
    }
  },
  methods: {
    pageChange(page) {
      this.$emit('page-change', page)
    },
    handleUpdate(value) {
      this.$emit('update-row', value)
    },
    handleDelete(value) {
      this.$emit('delete-row', value)
    }
  }
}
</script>

<style>
</style>

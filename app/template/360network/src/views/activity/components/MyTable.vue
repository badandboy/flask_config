<template>
  <div>
    <el-table :data="dataSource" style="width: 100%">
      <el-table-column type="index" width="50" />
      <el-table-column prop="title" label="活动名称" width="120" />

      <el-table-column prop="content" label="Banner">
        <template slot-scope="scoped">
          <img style="width: 220px;height: 220px; " :src="scoped.row.patch_img_url">
        </template>
      </el-table-column>
      <el-table-column prop="content" label="海报">
        <template slot-scope="scoped">
          <img style="width: 220px;height: 220px; " :src="scoped.row.poster_url">
        </template>
      </el-table-column>
      <el-table-column prop="content" label="内容">
        <template slot-scope="scoped">
          <img style="width: 220px;height: 220px; " :src="scoped.row.content_url">
        </template>
      </el-table-column>
      <el-table-column prop="enroll_start_at" label="开始时间" width="180" />
      <el-table-column prop="enroll_stop_at" label="结束时间" width="180" />
      <el-table-column prop="content" align="center" label="状态">
        <template slot-scope="{row}">
          <el-tag v-if="row.state == 1" type="success">开启中</el-tag>
          <el-tag v-else type="info">关闭</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="content" width="160" align="center" label="修改">
        <template slot-scope="{row}">
          <el-button type="primary" @click="handleUpdate(row)">修改</el-button>
          <el-button type="danger" @click="handleDelete(row)">删除</el-button>
        </template>
      </el-table-column>
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

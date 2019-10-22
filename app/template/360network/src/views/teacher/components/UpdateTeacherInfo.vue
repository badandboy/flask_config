<template>
  <el-dialog title="修改教师信息" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="姓名" prop="title">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="封面" prop="title">
        <upload :init-data="coverUrl" :images.sync="form.cover" />
      </el-form-item>
      <el-form-item label="内容" prop="title">
        <upload :init-data="contentUrl" :images.sync="form.content" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交修改</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
import Upload from '@/components/Upload'
import * as api from '@/api'
export default {
  components: {
    Upload
  },
  props: {
    visible: {
      type: Boolean,
      default: function() {
        return false
      }
    },
    dataSource: {
      type: Object,
      default: function() {
        return {}
      }
    }
  },
  data() {
    return {
      isLoading: false,
      dialogVisible: false,
      contentUrl: '',
      coverUrl: '',
      form: {
        title: '',
        cover: '',
        content: ''
      }
    }
  },
  watch: {
    dataSource: function(val) {
      if (Object.keys(val).length > 0) {
        this.form = {
          title: val.teacher_name || '',
          cover: val.teacher_cover_url,
          content: val.teacher_content_url
        }
        this.contentUrl = val.teacher_content_url
        this.coverUrl = val.teacher_cover_url
      }
    },
    visible: function(value) {
      this.dialogVisible = value
    },
    dialogVisible: function(value) {
      !value && this.$emit('update:visible', false)
    }
  },
  methods: {
    submitForm() {
      const { title, cover, content } = this.form
      if (!title || !cover || !content) {
        this.$message.error('请填写所有信息')
        return
      }
      api
        .updateTeacher({
          teacher_id: this.dataSource.teacher_id,
          teacher_name: title,
          teacher_cover_url: cover,
          teacher_content_url: content
        })
        .then(res => {
          if (res && res.code === '200') {
            this.$message.success('修改成功')
            this.$emit('success')
            this.dialogVisible = false
          } else {
            this.$message.error('修改失败')
          }
        })
    }
  }
}
</script>

<style></style>

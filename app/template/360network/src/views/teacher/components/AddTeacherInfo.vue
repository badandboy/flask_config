<template>
  <el-dialog title="新增教师信息" :visible.sync="dialogVisible">
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
      <el-form-item label="封面" prop="cover">
        <upload :images.sync="form.cover" />
      </el-form-item>
      <el-form-item label="内容" prop="content">
        <upload :images.sync="form.content" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">立即创建</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
import Upload from '@/components/Upload'
import * as Api from '@/api'
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
    }
  },
  data() {
    return {
      isLoading: false,
      dialogVisible: false,
      form: {
        title: '',
        cover: '',
        content: ''
      }
    }
  },
  watch: {
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
      Api.insertTeacher({
        teacher_name: title,
        teacher_cover_url: cover,
        teacher_content_url: content
      }).then(res => {
        if (res && res.code === '200') {
          this.$message.success('新增成功')
          this.$emit('succes')
          this.dialogVisible = false
          this.form = {
            title: '',
            cover: '',
            content: ''
          }
        } else {
          this.$message.error('新增失败')
        }
      })
    }
  }
}
</script>

<style></style>

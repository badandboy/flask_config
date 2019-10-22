<template>
  <el-dialog title="新增办学特色" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="内容" prop="content">
        <upload :images.sync="form.content" />
      </el-form-item>
      <el-form-item label="排序" prop="sort">
        <el-input v-model="form.sort" />
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
        sort: 0,
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
      const { sort, content } = this.form
      if (sort === '' || !content) {
        this.$message.error('请填写所有信息')
        return
      }
      Api.insertFeature({
        sort_value: sort,
        picture_url: content
      }).then(res => {
        if (res && res.code === '200') {
          this.$emit('success')
          this.$message.success('新增成功')
          this.dialogVisible = false
          this.form = {
            sort: '',
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

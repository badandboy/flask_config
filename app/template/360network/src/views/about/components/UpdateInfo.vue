<template>
  <el-dialog title="修改关于我们" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="封面" prop="title">
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
      form: {
        content: ''
      }
    }
  },
  watch: {
    dataSource: function(val) {
      if (Object.keys(val).length > 0) {
        this.form = {
          content: val.picture_url
        }
        this.contentUrl = val.picture_url
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
      const { content } = this.form
      if (!content) {
        this.$message.error('请填写所有信息')
        return
      }
      Api.updateAboutUs({
        picture_id: this.dataSource.picture_id,
        picture_url: content
      }).then(res => {
        if (res && res.code === '200') {
          this.$message.success('修改成功')
          this.$emit('success')
          this.dialogVisible = false
          this.form = {
            content: ''
          }
        } else {
          this.$message.error('修改失败')
        }
      })
    }
  }
}
</script>

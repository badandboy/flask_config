<template>
  <el-dialog title="修改办学特色" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="内容" prop="content">
        <upload :init-data="contentUrl" :images.sync="form.content" />
      </el-form-item>
      <el-form-item label="排序" prop="sort">
        <el-input v-model="form.sort" />
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
      form: {
        sort: 0,
        content: ''
      }
    }
  },
  watch: {
    dataSource: function(val) {
      if (Object.keys(val).length > 0) {
        this.form = {
          sort: val.sort,
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
      const { sort, content } = this.form
      if (!sort || !content) {
        this.$message.error('请填写所有信息')
        return
      }
      Api.updateFeature({
        picture_id: this.dataSource.picture_id,
        sort_value: sort,
        picture_url: content
      }).then(res => {
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

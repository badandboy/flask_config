<template>
  <el-dialog title="新增活动信息" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="活动名称" prop="title">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="Banner" prop="banner">
        <upload :images.sync="form.banner" />
      </el-form-item>
      <el-form-item label="海报" prop="cover">
        <upload :images.sync="form.cover" />
      </el-form-item>
      <el-form-item label="内容" prop="content">
        <upload :images.sync="form.content" />
      </el-form-item>
      <el-form-item label="开始时间" prop="name">
        <el-date-picker
          v-model="form.startTime"
          type="datetime"
          placeholder="选择日期时间"
          value-format="yyyy-MM-dd hh:mm:ss"
        />
      </el-form-item>
      <el-form-item label="结束时间" prop="name">
        <el-date-picker
          v-model="form.endTime"
          type="datetime"
          placeholder="选择日期时间"
          value-format="yyyy-MM-dd hh:mm:ss"
        />
      </el-form-item>
      <el-form-item label="是否开启" prop="state">
        <el-switch
          v-model="form.state"
          active-text="开启"
          inactive-text="关闭"
          :active-value="1"
          :inactive-value="0"
        />
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
        banner: '',
        cover: '',
        content: '',
        startTime: '',
        endTime: '',
        state: 1
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
      const {
        title,
        content,
        banner,
        cover,
        startTime,
        endTime,
        state
      } = this.form
      if (!title || !content || !banner || !cover || !startTime || !endTime) {
        this.$message.error('请填写所有信息')
        return
      }
      Api.insertActivity({
        title: title,
        patch_img_url: banner,
        poster_url: cover,
        content_url: content,
        enroll_start_at: startTime,
        enroll_stop_at: endTime,
        status: state
      }).then(res => {
        if (res && res.code === '200') {
          this.$message.success('新增成功')
          this.$emit('success')
          this.dialogVisible = false
          this.form = {
            title: '',
            banner: '',
            cover: '',
            content: '',
            startTime: '',
            endTime: '',
            state: 1
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

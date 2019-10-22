<template>
  <el-dialog title="修改活动信息" :visible.sync="dialogVisible">
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
        <upload :init-data="bannerUrl" :images.sync="form.banner" />
      </el-form-item>
      <el-form-item label="海报" prop="cover">
        <upload :init-data="coverUrl" :images.sync="form.cover" />
      </el-form-item>
      <el-form-item label="内容" prop="content">
        <upload :init-data="contentUrl" :images.sync="form.content" />
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
        <el-button type="primary" @click="submitForm">保存</el-button>
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
        title: '',
        banner: '',
        cover: '',
        content: '',
        startTime: '',
        endTime: '',
        state: 1
      },
      contentUrl: '',
      coverUrl: '',
      bannerUrl: ''
    }
  },
  watch: {
    dataSource: function(val) {
      if (Object.keys(val).length > 0) {
        this.form = {
          title: val.title || '',
          banner: val.patch_img_url || '',
          cover: val.poster_url || '',
          content: val.content_url || '',
          startTime: val.enroll_start_at || '',
          endTime: val.enroll_stop_at || '',
          state: val.status || ''
        }
        this.contentUrl = val.content_url
        this.coverUrl = val.poster_url
        this.bannerUrl = val.patch_img_url
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
      Api.updateActivity({
        activity_id: this.dataSource.activity_id,
        title: title,
        patch_img_url: banner,
        poster_url: cover,
        content_url: content,
        enroll_start_at: startTime,
        enroll_stop_at: endTime,
        status: state
      }).then(res => {
        if (res && res.code === '200') {
          this.$message.success('修改成功')
          this.$emit('succes')
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

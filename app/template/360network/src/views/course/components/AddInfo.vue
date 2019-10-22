<template>
  <el-dialog title="新增课程信息" :visible.sync="dialogVisible">
    <el-form
      v-if="dialogVisible"
      ref="ruleForm"
      :model="form"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="课程名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="讲师" prop="teacher">
        <el-select v-model="form.teacher" placeholder="请选择">
          <el-option
            v-for="item in teacherList"
            :key="item.teacher_id"
            :label="item.teacher_name"
            :value="item.teacher_id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="封面" prop="cover">
        <upload :images.sync="form.cover" />
      </el-form-item>
      <el-form-item label="内容" prop="content">
        <el-input v-model="form.content" />
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
    }
  },
  data() {
    return {
      isLoading: false,
      dialogVisible: false,
      contentUrl: '',
      coverUrl: '',
      form: {
        name: '',
        teacher: '',
        cover: '',
        content: ''
      },
      teacherList: []
    }
  },
  watch: {
    visible: function(value) {
      this.dialogVisible = value
      if (value) {
        this.getTeacherList()
      }
    },
    dialogVisible: function(value) {
      !value && this.$emit('update:visible', false)
    }
  },
  methods: {
    /**
     * 获取所有教师
     */
    getTeacherList() {
      Api.queryTeacherList().then(res => {
        if (res && res.code === '200') {
          this.teacherList = res.data
        }
      })
    },
    /**
     * 提交数据
     */
    submitForm() {
      const { name, teacher, cover, content } = this.form
      if (!name || !cover || !content || !teacher) {
        this.$message.error('请填写所有信息')
        return
      }
      const teacherName = this.teacherList.filter(
        item => item.teacher_id === teacher
      )
      Api.insertCourse({
        course_name: name,
        teacher_id: teacher,
        teacher_name: teacherName[0] && teacherName[0].teacher_name,
        course_cover_url: cover,
        course_content_url: content
      }).then(res => {
        if (res && res.code === '200') {
          this.$message.success('新增成功')
          this.$emit('success')
          this.dialogVisible = false
          this.form = {
            name: '',
            teacher: '',
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

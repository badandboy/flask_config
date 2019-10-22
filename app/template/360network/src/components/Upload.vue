<template>
  <div>
    <el-upload
      action="http://106.15.45.103/api/v1.0/uploadAvatar"
      :http-request="submitUpload"
      list-type="picture-card"
      :file-list="fileList"
      :on-preview="handlePictureCardPreview"
      :on-remove="handleRemove"
      :class="{ hide: hideUpload }"
      :on-change="hanldeChange"
      :on-success="handleSucess"
      :on-error="handleError"
    >
      <i class="el-icon-plus" />
    </el-upload>
    <!-- <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="dialogImageUrl" alt>
    </el-dialog>-->
  </div>
</template>

<script>
import * as api from '@/api'
export default {
  props: {
    images: {
      type: String,
      default: function() {
        return ''
      }
    },
    initData: {
      type: String,
      default: function() {
        return ''
      }
    }
  },
  data() {
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      hideUpload: false,
      limitCount: 1,
      fileList: []
    }
  },
  watch: {
    initData: {
      handler: function(val) {
        if (!val) {
          this.fileList = []
        } else if (Array.isArray(val)) {
          this.fileList = val
        } else {
          this.fileList = [
            {
              url: val,
              name: val
            }
          ]
        }
        this.hideUpload = this.fileList.length > 0
      },
      immediate: true
    }
  },
  methods: {
    handleRemove(file, fileList) {
      setTimeout(() => {
        this.hideUpload = fileList.length >= this.limitCount
      }, 300)
      this.$emit('change', fileList)
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    hanldeChange(file, fileList) {
      this.$emit('change', fileList)
      this.hideUpload = fileList.length >= this.limitCount
    },
    handleSucess(response, file, fileList) {
      console.log('response', response)
    },
    // 上传失败
    handleError(err, file, fileList) {
      console.log('err', err)
    },
    submitUpload: function(content) {
      // 自定义的上传图片的方法
      const formData = new FormData()
      formData.append('file', content.file)
      api
        .uploadImg(formData)
        .then(res => {
          console.log(res)
          if (res && res.code === '200') {
            const url = res.url
            this.$emit('update:images', url)
            this.$message.success('上传成功')
          } else {
            this.fileList = []
            this.checkLength()
            //  this.$message.error('上传失败')
          }
        })
        .catch(error => {
          // this.$message.error('上传失败')
          this.fileList = []
          this.checkLength()
          console.log(error)
        })
    },
    checkLength() {
      this.hideUpload = this.fileList.length >= this.limitCount
    }
  }
}
</script>

<style lang="scss" scoped>
/deep/ {
  .hide .el-upload--picture-card {
    display: none;
  }
  .el-upload-list__item-preview {
    display: none !important;
  }
}
</style>

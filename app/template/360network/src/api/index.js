import service from '@/utils/request'
import qs from 'qs'

export const login = params => {
  return service.post(`/v1.0/login`, qs.stringify(params))
}
// 上传图片
export const uploadImg = formData => {
  const config = {
    'Content-Type': 'multipart/form-data'
  }
  return service.post('/v1.0/uploadAvatar', formData, config)
}

// 查询教师
export const queryTeacher = params => {
  return service.post(`/v1.0/selTeacher`, qs.stringify(params))
}

// 新增教师
export const insertTeacher = params => {
  return service.post(`/v1.0/addTeacher`, qs.stringify(params))
}

// 修改教师
export const updateTeacher = params => {
  return service.post(`/v1.0/updTeacher`, qs.stringify(params))
}

// 删除教师
export const deleteTeacher = params => {
  return service.post(`/v1.0/delTeacher`, qs.stringify(params))
}

// 查询关于我们
export const queryAbout = params => {
  return service.post(`/v1.0/selAboutUs`, qs.stringify(params))
}

// 修改关于我们
export const updateAboutUs = params => {
  return service.post(`/v1.0/updAboutUs`, qs.stringify(params))
}

// 查询新闻列表
export const queryNews = params => {
  return service.post(`/v1.0/selNews`, qs.stringify(params))
}

// 新增新闻
export const insertNews = params => {
  return service.post(`/v1.0/addNews`, qs.stringify(params))
}

// 修改新闻
export const updateNews = params => {
  return service.post(`/v1.0/updNews`, qs.stringify(params))
}

// 删除新闻
export const deleteNews = params => {
  return service.post(`/v1.0/delNews`, qs.stringify(params))
}

// 查询体验者列表
export const queryExperiencer = params => {
  return service.post(`/v1.0/selExperiencers`, qs.stringify(params))
}

// 教师列表
export const queryTeacherList = params => {
  return service.post(`/v1.0/get_teacher_list`, qs.stringify(params))
}

// 查询课程列表
export const queryCourse = params => {
  return service.post(`/v1.0/get_course_list`, qs.stringify(params))
}

// 新增课程
export const insertCourse = params => {
  return service.post(`/v1.0/add_course`, qs.stringify(params))
}

// 修改课程
export const updatetCourse = params => {
  return service.post(`/v1.0/edit_course`, qs.stringify(params))
}

// 删除课程
export const deleteCourse = params => {
  return service.post(`/v1.0/del_course`, qs.stringify(params))
}

// 教学特色列表
export const queryFeature = params => {
  return service.post(`/v1.0/selSchoolFeature`, qs.stringify(params))
}

// 新增教学特色
export const insertFeature = params => {
  return service.post(`/v1.0/addSchoolFeature`, qs.stringify(params))
}

// 修改教学特色
export const updateFeature = params => {
  return service.post(`/v1.0/updSchoolFeature`, qs.stringify(params))
}

// 删除教学特色
export const deleteFeature = params => {
  return service.post(`/v1.0/delSchoolFeature`, qs.stringify(params))
}

// 查询活动列表
export const queryActivity = params => {
  return service.post(`/v1.0/get_activity_list`, qs.stringify(params))
}

// 新增活动Banner
export const insertActivity = params => {
  return service.post(`/v1.0/add_activity`, qs.stringify(params))
}

// 修改活动Banner
export const updateActivity = params => {
  return service.post(`/v1.0/edit_activity`, qs.stringify(params))
}

// 删除活动Banner
export const deleteActivity = params => {
  return service.post(`/v1.0/del_activity`, qs.stringify(params))
}

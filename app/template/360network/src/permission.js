import routers from '@/router'
import { getCookie } from '@/utils/cookie'

const whiteList = ['/login']

routers.beforeEach((to, from, next) => {
  if (whiteList.indexOf(to.path) !== -1) {
    // 在免登录白名单，直接进入
    next()
    return
  }
  if (getCookie('TOKEN') && getCookie('TOKEN') !== 'undefined') {
    next()
  } else {
    // 未登录
    next({
      path: '/login',
      query: {
        redirect: to.fullPath
      }
    })
  }
})

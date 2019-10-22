import Vue from 'vue'
import Router from 'vue-router'

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },
  // {
  //   path: '/dashboard',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'dashboard',
  //       name: 'Dashboard',
  //       component: () => import('@/views/dashboard/index'),
  //       meta: { title: 'Dashboard', icon: 'dashboard' }
  //     }
  //   ]
  // },
  {
    path: '/',
    component: Layout,
    redirect: '/experiencer',
    children: [
      {
        path: 'experiencer',
        name: 'experiencer',
        component: () => import('@/views/experiencer/index'),
        meta: { title: '首页', icon: 'dashboard' }
      }
    ]
  },

  {
    path: '/teacher',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'teacher',
        component: () => import('@/views/teacher/index'),
        meta: { title: '师资力量', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/course',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'course',
        component: () => import('@/views/course/index'),
        meta: { title: '课程列表', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/activity',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'news',
        component: () => import('@/views/activity/index'),
        meta: { title: '活动信息', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/news',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'news',
        component: () => import('@/views/news/index'),
        meta: { title: '新闻动态', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/feature',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'feature',
        component: () => import('@/views/feature/index'),
        meta: { title: '教学特色', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/about',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'about',
        component: () => import('@/views/about/index'),
        meta: { title: '关于我们', icon: 'dashboard' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

Vue.use(Router)
const router = new Router({
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

export default router

import Cookies from 'js-cookie'
const ExpiresTime = 1 / 4

/**
 * 设置Cookie
 * @param  {[ key ]} 键
 * @param  {[ value ]} 值
 * @param  {[ params ]} 其他参数
 * @return {[ null ]}
 */
export const setCookie = (
  key,
  value,
  params = {
    expires: ExpiresTime
  }
) => {
  Cookies.set(key, value, params)
}

/**
 * 设置Cookie
 * @param  {[ key ]} 键
 * @return {[ String ]} Cookie 值
 */
export const getCookie = key => {
  return Cookies.get(key)
}

/**
 * 移除Cookie
 * @param  {[ key ]} 键
 * @return {[ null ]}
 */
export const removeCookie = key => {
  Cookies.remove(key)
}

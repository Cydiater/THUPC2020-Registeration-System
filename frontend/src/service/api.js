export default {
  LOGIN: {
    url: '/auth/login',
    method: 'post',
  },
  REGISTER: {
    url: '/auth/register',
    method: 'post',
  },
  USERINFO: {
    url: '/api/userinfo',
    method: 'get',
  },
  POSTANNOUNCEMENT: {
    url: '/api/postboard',
    method: 'post',
  },
  GETANNOUNCEMENTS: {
    url: '/api/postboard',
    method: 'get',
  },
  EDITPROFILE: {
    url: '/api/userinfo',
    method: 'post',
  },
  GETEMAILSTATUS: {
    url: '/api/email',
    method: 'get',
  },
  CHECKEMAIL: {
    url: '/api/email',
    method: 'post',
  },
}

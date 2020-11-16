import API from './api';
import router from '@/router';
import { authHeader } from '@/utils';

function handleResponse(response) {
  return response.json()
  .then(json => {
    if (!response.ok) {
      if (response.status == 401 && router.history.current.name != 'login') {
        logout();
        location.reload(true);
      }
      const error = json.message || response.statusText;
      return Promise.reject(error);
    }
    return json;
  });
}

function login(username, password) {
  const requestOptions = {
    method: API.LOGIN.method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      username,
      password
    })
  };

  return fetch(API.LOGIN.url, requestOptions)
  .then(handleResponse)
  .then(auth => {
    if (auth.token) {
      localStorage.setItem('token', auth.token);
      return auth;
    }
    return Promise.reject(auth.message);
  });
}

function logout() {
  localStorage.removeItem('token');
  localStorage.removeItem('username');
}

function register(username, password, type, members) {
  const requestOptions = {
    method: API.REGISTER.method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      teamname: username,
      password,
      type,
      members,
    })
  };
  return fetch(API.REGISTER.url, requestOptions)
  .then(handleResponse);
}

function userinfo(username) {
  const requestOptions = {
    method: API.USERINFO.method,
    headers: authHeader(),
  };
  return fetch(API.USERINFO.url + '?name=' + username, requestOptions)
  .then(handleResponse);
}

function postAnnouncement(id, title, content, author, timestamp) {
  const body = {
    title,
    content,
    author,
    timestamp,
  };
  if (id === 0 || id)
    body.id = id;

  const requestOptions = {
    method: API.POSTANNOUNCEMENT.method,
    headers: authHeader(),
    body: JSON.stringify(body)
  };
  return fetch(API.POSTANNOUNCEMENT.url, requestOptions)
  .then(handleResponse);
}

function getAnnouncements() {
  const requestOptions = {
    method: API.GETANNOUNCEMENTS.method,
    headers: authHeader(),
  };
  return fetch(API.GETANNOUNCEMENTS.url, requestOptions)
  .then(handleResponse);
}

function editProfile(members) {
  const requestOptions = {
    method: API.EDITPROFILE.method,
    headers: authHeader(),
    body: JSON.stringify({ members }),
  };
  return fetch(API.EDITPROFILE.url, requestOptions)
  .then(handleResponse);
}

export default {
  login,
  logout,
  register,
  userinfo,
  postAnnouncement,
  getAnnouncements,
  editProfile,
}

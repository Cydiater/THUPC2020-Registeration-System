import API from './api';
import router from '@/router';

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
}

function register(username, password, email, type, members) {
  const requestOptions = {
    method: API.REGISTER.method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      teamname: username,
      password,
      email,
      type,
      members,
    })
  };
  return fetch(API.REGISTER.url, requestOptions)
  .then(handleResponse);
}

export default {
  login,
  logout,
  register,
}

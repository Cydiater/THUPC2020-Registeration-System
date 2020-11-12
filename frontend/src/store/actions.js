import { userService } from '@/service';

export default {
  loginRequest({ commit, dispatch }, { username, password }) {
    commit('setStatus', 'waitForLogin');
    commit('setUsername', username);
    userService.login(username, password)
    .then(res => {
      dispatch('loginSuccess', res.token);
    }, error => {
      dispatch('loginFailed', error);
    });
  },
  loginSuccess({ commit, dispatch }, token) {
    commit('clearStatus', 'waitForLogin');
    commit('clearStatus', 'loggingIn');
    commit('setToken', token);
    commit('notify', { type: 'success', message: 'Login Success' });
    dispatch('fetchUserInfo');
  },
  loginFailed({ commit }, error) {
    commit('clearStatus', 'waitForLogin');
    commit('clearStatus', 'loggingIn');
    commit('notify', { type: 'error', message: error });
  },
  registerRequest({ commit, dispatch }, { username, password, email, type, members }) {
    commit('setStatus', 'waitForRegister');
    userService.register(username, password, email, type.toLowerCase(), members)
    .then(() => {
      dispatch('registerSuccess');
    }, error => {
      dispatch('registerFailed', error);
    });
  },
  registerSuccess({ commit }) {
    commit('clearStatus', 'waitForRegister');
    commit('clearStatus', 'registering');
    commit('notify', { type: 'success', message: 'Sign up Success' });
  },
  registerFailed({ commit }, error) {
    commit('clearStatus', 'waitForRegister');
    commit('clearStatus', 'registering');
    commit('notify', { type: 'error', message: error });
  },
  fetchUserInfo({ commit }, username) {
    userService.userinfo(username)
    .then(user => {
      commit('setUser', user);
    }, error => {
      commit('notify', { type: 'error', message: error });
    }) 
  },
  logout({ commit }) {
    userService.logout();
    commit('clearAll');
  }
};

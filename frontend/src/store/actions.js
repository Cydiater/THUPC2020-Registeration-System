import { userService } from '@/service';

export default {
  loginRequest({ commit, dispatch }, { username, password }) {
    commit('setStatus', 'waitForLogin');
    userService.login(username, password)
    .then(() => {
      dispatch('loginSuccess');
    }, error => {
      dispatch('loginFailed', error);
    });
  },
  loginSuccess({ commit }) {
    commit('clearStatus', 'waitForLogin');
    commit('clearStatus', 'loggingIn');
    commit('notify', { type: 'success', message: 'Login Success' });
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
  }
};

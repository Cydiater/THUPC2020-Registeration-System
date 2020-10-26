import Vue from 'vue';

export default {
  notify(state, { type, message }) {
    state.notification.show = true;
    state.notification.type = type;
    state.notification.message = message;
  },
  toggleNotification(state, value) {
    state.notification.show = value;
  },
  setStatus(state, status) {
    Vue.set(state.status, status, true);
  },
  clearStatus(state, status) {
    Vue.delete(state.status, status);
  }
};

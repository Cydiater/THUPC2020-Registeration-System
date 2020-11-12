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
  setToken(state, token) {
    state.token = token;
  },
  clearStatus(state, status) {
    Vue.delete(state.status, status);
  },
  setUser(state, user) {
    state.user = user;
  },
  setUsername(state, username) {
    state.username = username;
    localStorage.setItem('username', username);
  },
  clearAll(state) {
    state.status = {};
    state.token = null;
    state.notification =  {
        show: false,
        type: null,
        message: null,
      };
    state.user = null;
    state.username = null;
    state.announcements = [];
    state.currentAnnouncement = null;
  },
  setAnnouncements(state, announcements) {
    state.announcements = announcements;
  },
  toggleAnnouncement(state, announcement) {
    announcement.show = !announcement.show;
  },
  setCurrentAnnouncement(state, announcement) {
    state.currentAnnouncement = announcement;
  }
};

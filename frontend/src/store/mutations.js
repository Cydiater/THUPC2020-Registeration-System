export default {
  openLoginDialog(state) {
    state.status = 'loggingIn';
  },
  closeLoginDialog(state) {
    state.status = null;
  }
};

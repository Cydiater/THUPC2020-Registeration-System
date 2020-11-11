function isLoggedIn(state) {
  return Boolean(state.token);
}

export default {
  isLoggedIn,
};

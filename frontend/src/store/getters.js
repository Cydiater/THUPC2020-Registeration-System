function isLoggedIn(state) {
  return Boolean(state.token);
}

function isAdmin(state) {
  if (state.user)
    return Boolean(state.user.isAdmin);
  return false;
}

export default {
  isLoggedIn,
  isAdmin,
};

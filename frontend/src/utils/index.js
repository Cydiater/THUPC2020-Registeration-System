function authHeader() {
  const token = localStorage.getItem('token');
  return token ? { 'Authorzation': 'Bearer ' + token } : {};
}

export {
  authHeader,
}

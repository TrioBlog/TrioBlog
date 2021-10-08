import VueRouter from 'vue-router'
import Home from './page/Home'
import SignIn from './page/SignIn'
import SignUp from './page/SignUp'
// import Post from './components/Post'


const routes = [
  {path:'/home', component:Home, name:'Home'},
  {path: '/signin', component:SignIn, name:'SignIn' },
  {path: '/', component:SignUp, name:'SignUp' },
  // {path: '/posts', component:Post, name:'Post' }
]

export default new VueRouter({ routes, mode: 'history' })
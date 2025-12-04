<template>
	<div>
		<div id="particles"></div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__">
				<div class="login_form2">
					<div class="title-container">基于机器学习的电商评论情感分析</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
							<el-button type="primary" @click="register('yonghu')" class="register">
								注册用户							</el-button>
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	require('@/utils/particles.js')
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
				particlesJson: {"retina_detect":true,"particles":{"number":{"density":{"value_area":800,"enable":true},"value":150},"move":{"straight":false,"random":false,"bounce":false,"enable":true,"attract":{"rotateX":3000,"enable":false,"rotateY":3000},"speed":2,"direction":"none","out_mode":"out"},"color":{"value":"#fff"},"shape":{"image":{"width":100,"src":"img/github.svg","height":100},"polygon":{"nb_sides":5},"type":"circle","stroke":{"color":"#000000","width":0}},"size":{"anim":{"size_min":0,"sync":false,"enable":false,"speed":20},"random":false,"value":2},"line_linked":{"width":1,"distance":100,"color":"#ffffff","opacity":1,"enable":true},"opacity":{"anim":{"opacity_min":0,"sync":false,"enable":false,"speed":1},"random":false,"value":0.5}},"interactivity":{"detect_on":"canvas","events":{"resize":true,"onclick":{"mode":"push","enable":true},"onhover":{"mode":"grab","enable":true}},"modes":{"grab":{"distance":100,"line_linked":{"opacity":1}},"bubble":{"duration":0.7,"distance":200,"size":80,"opacity":0,"speed":3},"repulse":{"duration":0.4,"distance":200},"push":{"particles_nb":4},"remove":{"particles_nb":2}}}}
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

			particlesJS('particles',this.particlesJson);
		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						if(this.boardAuth('hasBoard','查看',this.rulesForm.role)) {
							this.$router.replace({ path: "/board" });
						}else {
							this.$router.replace({ path: "/" });
						}
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240926/67d8b8cb5e9e4bce9d9e8a301757a3ed.jpg) no-repeat center center / 100% 100%;
	background: url(http://codegen.caihongy.cn/20240926/67d8b8cb5e9e4bce9d9e8a301757a3ed.jpg) no-repeat center center / 100% 100%;
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	position: relative !important;

	.login_form {
		border-radius: 10px;
		padding: 20px 50px 60px;
		margin: 0 auto;
		z-index: 1002;
		background: rgba(77,151,195,.9);
		width: 600px;
		height: auto;
		.login_form2 {
			width: 100%;
			position: relative;
		}
		.title-container {
			padding: 0;
			margin: 0 0 20px 0;
			color: #2d4448;
			background: none;
			font-weight: 600;
			width: 100%;
			font-size: 22px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			border-radius: 8px;
			padding: 0 10px;
			margin: 0 0 20px;
			background: #fff;
			display: flex;
			width: calc(100% - 0px);
			border-color: #d5d0cd;
			border-width: 4px 0 0;
			align-items: center;
			position: relative;
			border-style: solid;
			flex-wrap: wrap;
			.lable {
				color: #000;
				width: auto;
				font-size: 16px;
				border-color: #d2d2d2;
				border-width: 0 1px 0 0;
				line-height: 30px;
				border-style: solid;
				text-align: right;
				min-width: 88px;
			}
			input {
				border: 0px solid #e6e6e6;
				border-radius: 0px;
				padding: 0 10px;
				color: #666;
				flex: 1;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			input:focus {
				border: 0px solid #e6e6e6;
				padding: 0 10px;
				color: #666;
				flex: 1;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.password-box {
				flex: 1;
				display: flex;
				width: 100%;
				position: relative;
				align-items: center;
				input {
					border: 0px solid #e6e6e6;
					padding: 0 10px;
					color: #666;
					background: none;
					width: 100%;
					font-size: 14px;
					height: 44px;
				}
				input:focus {
					border: 0px solid #e6e6e6;
					padding: 0 10px;
					color: #666;
					background: none;
					width: 100%;
					font-size: 14px;
					height: 44px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					line-height: 44px;
					position: absolute;
					right: 5px;
				}
			}
			input::placeholder {
				color: #8890a0;
				font-size: 16px;
			}
		}
		.list-type {
			padding: 0 0 0 15px;
			margin: 0;
			background: none;
			flex: 1;
			width: calc(100% - 0px);
			line-height: 40px;
			height: auto;
			/deep/ .el-radio__input .el-radio__inner {
				background: rgba(53, 53, 53, 0);
				border-color: #666;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: #016ba9;
				border-color: #016ba9;
			}
			/deep/ .el-radio__label {
				color: #666;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #016ba9;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 20px auto 0;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				padding: 0 120px 0 0;
				width: 100%;
				text-align: center;
				order: 3;
			}
			.login-btn2 {
				margin: 20px 0;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				flex-wrap: wrap;
			}
			.login-btn3 {
				width: 100%;
				text-align: center;
				order: -1;
			}
			.loginInBt {
				border: 10px solid #f9f9f9;
				cursor: pointer;
				padding: 0 10px;
				margin: 0 auto 10px;
				color: #fff;
				bottom: -124px;
				font-weight: 600;
				font-size: 22px;
				border-radius: 100%;
				box-shadow: inset 12px 0px 16px 0px #3d9cb2;
				background: #4dc2de;
				width: auto;
				position: absolute;
				min-width: 110px;
				height: 110px;
			}
			.loginInBt:hover {
				opacity: 1;
			}
			.register {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				padding: 0 10px;
				margin: 0 20px 10px 0;
				color: #333;
				font-size: 16px;
				border-color: #d5d0cd;
				border-radius: 10px;
				background: #fff;
				width: auto;
				border-width: 4px 0 0 ;
				border-style: solid;
				height: 44px;
			}
			.register:hover {
				opacity: 1;
			}
			.forget {
				border: 0px solid #FC4349;
				cursor: pointer;
				border-radius: 0;
				padding: 0 0px;
				margin: 0px 0px 0px 0;
				color: #333;
				background: none;
				width: auto;
				font-size: 16px;
				text-align: center;
				height: 34px;
			}
			.forget:hover {
				opacity: 1;
			}
		}
	}
}

	#particles{
		background-repeat: no-repeat;
		z-index: 1;
		background-size: cover;
		width: 100%;
		position: absolute;
		background-position: 50% 50%;
		height: 100%;
	}
</style>

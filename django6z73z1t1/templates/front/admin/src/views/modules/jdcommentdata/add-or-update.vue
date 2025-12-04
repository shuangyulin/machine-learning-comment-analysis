<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="input" v-if="type!='info'"  label="评论ID" prop="commentid" >
					<el-input v-model="ruleForm.commentid" placeholder="评论ID" clearable  :readonly="ro.commentid"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="评论ID" prop="commentid" >
					<el-input v-model="ruleForm.commentid" placeholder="评论ID" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="商品ID" prop="productid" >
					<el-input v-model="ruleForm.productid" placeholder="商品ID" clearable  :readonly="ro.productid"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="商品ID" prop="productid" >
					<el-input v-model="ruleForm.productid" placeholder="商品ID" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="SKUID" prop="skuid" >
					<el-input v-model="ruleForm.skuid" placeholder="SKUID" clearable  :readonly="ro.skuid"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="SKUID" prop="skuid" >
					<el-input v-model="ruleForm.skuid" placeholder="SKUID" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="行业" prop="industry" >
					<el-input v-model="ruleForm.industry" placeholder="行业" clearable  :readonly="ro.industry"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="行业" prop="industry" >
					<el-input v-model="ruleForm.industry" placeholder="行业" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="品牌" prop="brand" >
					<el-input v-model="ruleForm.brand" placeholder="品牌" clearable  :readonly="ro.brand"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="品牌" prop="brand" >
					<el-input v-model="ruleForm.brand" placeholder="品牌" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="商品系列" prop="productseries" >
					<el-input v-model="ruleForm.productseries" placeholder="商品系列" clearable  :readonly="ro.productseries"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="商品系列" prop="productseries" >
					<el-input v-model="ruleForm.productseries" placeholder="商品系列" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="型号" prop="model" >
					<el-input v-model="ruleForm.model" placeholder="型号" clearable  :readonly="ro.model"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="型号" prop="model" >
					<el-input v-model="ruleForm.model" placeholder="型号" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="SKU属性" prop="skuattribute" >
					<el-input v-model="ruleForm.skuattribute" placeholder="SKU属性" clearable  :readonly="ro.skuattribute"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="SKU属性" prop="skuattribute" >
					<el-input v-model="ruleForm.skuattribute" placeholder="SKU属性" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="用户信息" prop="userinformation" >
					<el-input v-model="ruleForm.userinformation" placeholder="用户信息" clearable  :readonly="ro.userinformation"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="用户信息" prop="userinformation" >
					<el-input v-model="ruleForm.userinformation" placeholder="用户信息" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="评分明细" prop="ratingdetails" >
					<el-input v-model="ruleForm.ratingdetails" placeholder="评分明细" clearable  :readonly="ro.ratingdetails"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="评分明细" prop="ratingdetails" >
					<el-input v-model="ruleForm.ratingdetails" placeholder="评分明细" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="客户端" prop="client" >
					<el-input v-model="ruleForm.client" placeholder="客户端" clearable  :readonly="ro.client"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="客户端" prop="client" >
					<el-input v-model="ruleForm.client" placeholder="客户端" readonly></el-input>
				</el-form-item>
				<el-form-item class="date" v-if="type!='info'" label="评价时间" prop="evaluationtime" >
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.evaluationtime" 
						type="datetime"
						:readonly="ro.evaluationtime"
						placeholder="评价时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item class="input" v-else-if="ruleForm.evaluationtime" label="评价时间" prop="evaluationtime" >
					<el-input v-model="ruleForm.evaluationtime" placeholder="评价时间" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="商家回复" prop="merchantresponse" >
					<el-input v-model="ruleForm.merchantresponse" placeholder="商家回复" clearable  :readonly="ro.merchantresponse"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="商家回复" prop="merchantresponse" >
					<el-input v-model="ruleForm.merchantresponse" placeholder="商家回复" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="带图评论" prop="commentswithpictures" >
					<el-input v-model="ruleForm.commentswithpictures" placeholder="带图评论" clearable  :readonly="ro.commentswithpictures"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="带图评论" prop="commentswithpictures" >
					<el-input v-model="ruleForm.commentswithpictures" placeholder="带图评论" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="追评内容" prop="followupreviewcontent" >
					<el-input v-model="ruleForm.followupreviewcontent" placeholder="追评内容" clearable  :readonly="ro.followupreviewcontent"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="追评内容" prop="followupreviewcontent" >
					<el-input v-model="ruleForm.followupreviewcontent" placeholder="追评内容" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="追评时间" prop="reviewtime" >
					<el-input v-model="ruleForm.reviewtime" placeholder="追评时间" clearable  :readonly="ro.reviewtime"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="追评时间" prop="reviewtime" >
					<el-input v-model="ruleForm.reviewtime" placeholder="追评时间" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="textarea" v-if="type!='info'" label="评价内容" prop="evaluationcontent" >
				<el-input
					style="min-width: 200px; max-width: 600px;"
					type="textarea"
					:rows="8"
					placeholder="评价内容"
					v-model="ruleForm.evaluationcontent" >
				</el-input>
			</el-form-item>
			<el-form-item v-else-if="ruleForm.evaluationcontent" label="评价内容" prop="evaluationcontent" >
				<span class="text">{{ruleForm.evaluationcontent}}</span>
			</el-form-item>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					确定
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	export default {
		data() {
			return {
				id: '',
				type: '',
			
			
				ro:{
					commentid : false,
					productid : false,
					skuid : false,
					industry : false,
					brand : false,
					productseries : false,
					model : false,
					skuattribute : false,
					userinformation : false,
					evaluationcontent : false,
					ratingdetails : false,
					client : false,
					evaluationtime : false,
					merchantresponse : false,
					commentswithpictures : false,
					followupreviewcontent : false,
					reviewtime : false,
				},
			
				ruleForm: {
					commentid: '',
					productid: '',
					skuid: '',
					industry: '',
					brand: '',
					productseries: '',
					model: '',
					skuattribute: '',
					userinformation: '',
					evaluationcontent: '',
					ratingdetails: '',
					client: '',
					evaluationtime: '',
					merchantresponse: '',
					commentswithpictures: '',
					followupreviewcontent: '',
					reviewtime: '',
				},

				rules: {
					commentid: [
					],
					productid: [
					],
					skuid: [
					],
					industry: [
					],
					brand: [
					],
					productseries: [
					],
					model: [
					],
					skuattribute: [
					],
					userinformation: [
					],
					evaluationcontent: [
					],
					ratingdetails: [
					],
					client: [
					],
					evaluationtime: [
					],
					merchantresponse: [
					],
					commentswithpictures: [
					],
					followupreviewcontent: [
					],
					reviewtime: [
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
					for (var o in obj){
						if(o=='commentid'){
							this.ruleForm.commentid = obj[o];
							this.ro.commentid = true;
							continue;
						}
						if(o=='productid'){
							this.ruleForm.productid = obj[o];
							this.ro.productid = true;
							continue;
						}
						if(o=='skuid'){
							this.ruleForm.skuid = obj[o];
							this.ro.skuid = true;
							continue;
						}
						if(o=='industry'){
							this.ruleForm.industry = obj[o];
							this.ro.industry = true;
							continue;
						}
						if(o=='brand'){
							this.ruleForm.brand = obj[o];
							this.ro.brand = true;
							continue;
						}
						if(o=='productseries'){
							this.ruleForm.productseries = obj[o];
							this.ro.productseries = true;
							continue;
						}
						if(o=='model'){
							this.ruleForm.model = obj[o];
							this.ro.model = true;
							continue;
						}
						if(o=='skuattribute'){
							this.ruleForm.skuattribute = obj[o];
							this.ro.skuattribute = true;
							continue;
						}
						if(o=='userinformation'){
							this.ruleForm.userinformation = obj[o];
							this.ro.userinformation = true;
							continue;
						}
						if(o=='evaluationcontent'){
							this.ruleForm.evaluationcontent = obj[o];
							this.ro.evaluationcontent = true;
							continue;
						}
						if(o=='ratingdetails'){
							this.ruleForm.ratingdetails = obj[o];
							this.ro.ratingdetails = true;
							continue;
						}
						if(o=='client'){
							this.ruleForm.client = obj[o];
							this.ro.client = true;
							continue;
						}
						if(o=='evaluationtime'){
							this.ruleForm.evaluationtime = obj[o];
							this.ro.evaluationtime = true;
							continue;
						}
						if(o=='merchantresponse'){
							this.ruleForm.merchantresponse = obj[o];
							this.ro.merchantresponse = true;
							continue;
						}
						if(o=='commentswithpictures'){
							this.ruleForm.commentswithpictures = obj[o];
							this.ro.commentswithpictures = true;
							continue;
						}
						if(o=='followupreviewcontent'){
							this.ruleForm.followupreviewcontent = obj[o];
							this.ro.followupreviewcontent = true;
							continue;
						}
						if(o=='reviewtime'){
							this.ruleForm.reviewtime = obj[o];
							this.ro.reviewtime = true;
							continue;
						}
					}
				}
				// 获取用户信息
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						var json = data.data;
					} else {
						this.$message.error(data.msg);
					}
				});
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `jdcommentdata/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					var objcross = this.$storage.getObj('crossObj');
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `jdcommentdata/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.jdcommentdataCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});
						}
					});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.jdcommentdataCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 30px 40px;
	}
	.add-update-preview {
		border-radius: 10px;
		padding: 40px 30% 40px 10%;
		background: #fff;
		border-color: #eee;
		border-width: 0px 0 0;
		border-style: solid;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 26px 0;
		display: inline-block;
		width: 100%;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #6e6e6e;
		font-weight: 500;
		width: 180px;
		font-size: 15px;
		line-height: 40px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	.add-update-preview .el-form-item span.text {
		padding: 0 10px;
		color: #666;
		background: none;
		font-weight: 500;
		display: inline-block;
		font-size: 15px;
		line-height: 40px;
		min-width: 100%;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 15px;
		min-width: 50%;
		height: 40px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 0px solid #ccc;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 15px;
		min-width: 50%;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 0px solid #ccc;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 10px;
		color: #666;
		width: 100%;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 0;
		cursor: not-allowed;
		border-radius: 4px;
		padding: 0 10px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 34px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #666;
		background: #fff;
		width: 100%;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 0;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .viewBtn {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 0;
		cursor: not-allowed;
		border-radius: 4px;
		padding: 0 0px;
		margin: 0 20px 0 0;
		outline: none;
		color: #999;
		background: none;
		width: auto;
		font-size: 15px;
		line-height: 40px;
		height: 40px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 12px;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		min-width: 100%;
		height: 120px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 0;
				cursor: not-allowed;
				border-radius: 0px;
				padding: 12px;
				color: #666;
				background: none;
				width: auto;
				font-size: 15px;
				min-width: 400px;
				height: auto;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 20px 0 0;
		width: 100%;
		text-align: left;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #4dc2de;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #2879f0;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #32c67a;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #98a58f;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #3fa2d1;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>

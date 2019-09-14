var flg=0;
function fun(){
	console.log("generate text...");
	$.ajax({
		method: "POST",
		url:"ret",
		data:{
			csrfmiddlewaretoken:'{{ csrf_token }}',
		},
		success:function(data){
			//console.log(data)
			var d=document.getElementById('generate');
			d.innerHTML=data;
		}
	});
}
function rec_noise(){
	console.log("===start record(noise)===")
	var d=document.getElementById('rec_noise');
	d.className = "ui primary loading button";
	function enable_all(){
		var d=document.getElementById('rec1');
		d.className = "ui orange button";
		var d=document.getElementById('rec2');
		d.className = "ui orange button";
		var d=document.getElementById('rec3');
		d.className = "ui orange button";
		var d=document.getElementById('rec4');
		d.className = "ui orange button";
		var d=document.getElementById('rec5');
		d.className = "ui orange button";
	}

	$.ajax({
			url:"rec_noise",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record(noise)===")
				var d=document.getElementById('rec_noise');
				d.className = "ui disabled large teal button";
				d.innerHTML="Noise<br>Recorded!!!";
				enable_all();
			}
		});
}
function rec1(){
	window.flg++;
	console.log("===start record 1===")
	var d=document.getElementById('rec1');
	d.className = "ui primary loading button";
	d.innerHTML = "Recording...";
	$.ajax({
			url:"rec1",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record 1===")
				var d=document.getElementById('rec1');
				d.className = 'ui disabled orange button';
				d.innerHTML="Recorded&nbsp;&nbsp;&nbsp;";
				var ip=document.createElement('i');
				ip.className = "thumbs up icon";
				d.appendChild(ip);
				if(window.flg == 5){
					var d=document.getElementById('submit_2');
					d.className = 'ui green button';
				}
			}
		});
}
function rec2(){
	window.flg++;
	console.log("===start record 2===")
	var d=document.getElementById('rec2');
	d.className = "ui primary loading button";
	$.ajax({
			url:"rec2",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record 2===")
				var d=document.getElementById('rec2');
				d.className = 'ui disabled orange button';
				d.innerHTML="Recorded&nbsp;&nbsp;&nbsp;";
				var ip=document.createElement('i');
				ip.className = "thumbs up icon";
				d.appendChild(ip);
				if(window.flg == 5){
					var d=document.getElementById('submit_2');
					d.className = 'ui green button';
				}
			}
	});
}
function rec3(){
	window.flg++;
	console.log("===start record 3===")
	var d=document.getElementById('rec3');
	d.className = "ui primary loading button";
	$.ajax({
			url:"rec3",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record 3===")
				var d=document.getElementById('rec3');
				d.className = 'ui disabled orange button';
				d.innerHTML="Recorded&nbsp;&nbsp;&nbsp;";
				var ip=document.createElement('i');
				ip.className = "thumbs up icon";
				d.appendChild(ip);
				if(window.flg == 5){
					var d=document.getElementById('submit_2');
					d.className = 'ui green button';
				}
			}
		});
}
function rec4(){
	window.flg++;
	console.log("===start record 4===")
	var d=document.getElementById('rec4');
	d.className = "ui primary loading button";
	$.ajax({
			url:"rec4",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record 4===")
				var d=document.getElementById('rec4');
				d.className = 'ui disabled orange button';
				d.innerHTML="Recorded&nbsp;&nbsp;&nbsp;";
				var ip=document.createElement('i');
				ip.className = "thumbs up icon";
				d.appendChild(ip);
				if(window.flg == 5){
					var d=document.getElementById('submit_2');
					d.className = 'ui green button';
				}
			}
		});
}
function rec5(){
	window.flg++;
	console.log("===start record 5===")
	var d=document.getElementById('rec5');
	d.className = "ui primary loading button";
	$.ajax({
			url:"rec5",
			data:{
				csrfmiddlewaretoken:'{{ csrf_token }}',
			},
			success:function(data){
				console.log("===done record 5===")
				var d=document.getElementById('rec5');
				d.className = 'ui disabled orange button';
				d.innerHTML="Recorded&nbsp;&nbsp;&nbsp;";
				var ip=document.createElement('i');
				ip.className = "thumbs up icon";
				d.appendChild(ip);
				if(window.flg == 5){
					var d=document.getElementById('submit_2');
					d.className = 'ui green button';
				}
			}
		});
}
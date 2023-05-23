$(function () {


	//CART

	$('.add-to-cart').on('click', function (e) {

		e.preventDefault(); // отменяет переход по ссылки
		const id = $(this).data('id'); // id товара, количество ели есть else :1
		const type = $(this).data('type');
		const slug = $(this).data('slug')
		const $this = $(this); // текущий объект по которому был клик
		console.log(type, id);


		$.ajax({
			url: "/cart/cart_add/", //  url на который мы хотим отправить данные 

			type: 'GET',
			data: { type: type, id: id, slug: slug },
			success: function (res) {  // сохраняем ответ в переменную res
				console.log(res)	
			},
			error: function () {
				alert('Error!')
			}

		})
		
		});


//CART


	$('.open-search').click(function (e) {
		e.preventDefault();
		$('#search').addClass('active');
	});
	$('.close-search').click(function () {
		$('#search').removeClass('active');
	});

	$(window).scroll(function () {
		if ($(this).scrollTop() > 200) {
			$('#top').fadeIn();
		} else {
			$('#top').fadeOut();
		}
	});

	$('#top').click(function () {
		$('body, html').animate({ scrollTop: 0 }, 700);
	});

	$('.sidebar-toggler .btn').click(function () {
		$('.sidebar-toggle').slideToggle();
	});

	// $('.thumbnails').magnificPopup({
	// 	type: 'image',
	// 	delegate: 'a',
	// 	gallery: {
	// 		enabled: true
	// 	},
	// 	removalDelay: 500,
	// 	callbacks: {
	// 		beforeOpen: function () {
	// 			this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
	// 			this.st.mainClass = this.st.el.attr('data-effect');
	// 		}
	// 	}
	// });

});
jQuery(document).ready(function () {
    (function($) {
        $.fn.inputFilter = function(inputFilter) {
          return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function() {
            if (inputFilter(this.value)) {
              this.oldValue = this.value;
              this.oldSelectionStart = this.selectionStart;
              this.oldSelectionEnd = this.selectionEnd;
            } else if (this.hasOwnProperty("oldValue")) {
              this.value = this.oldValue;
              this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
            }
          });
        };
      }(jQuery));
    $("#id_ISBN").inputFilter(function(value) {
        return /^\d*$/.test(value);
      });
    $("#enviar").click(function () {

        var codigo = $("#id_ISBN").val();
        var nombreLibro = $("#id_nombreLibro").val();
        var descripcion = $("#id_descripcion").val();
        var categoria = $("#id_categoria").val();
        
        var mensaje = "";

        if (codigo !== "") {

            if (codigo.length !== 13) {

                mensaje += "ISBN no es correcto, son 13 numeros!\n";
            }

        } else {

            mensaje += "Ingrese ISBN \n";
        }
        if (nombreLibro == "") {

            mensaje += "Ingrese Nombre del libro \n";

        }
        if (descripcion == "") {

            mensaje += "Ingrese descripcion \n";

        }
        if (categoria == "") {

            mensaje += "Seleccione categoria \n";

        }
        if (mensaje !== "") {

            alert(mensaje);
            return false;

        }

    });

    $("#enviarUsuario").click(function () {

        var nombre = $("#id_nombre").val();
        var apellido = $("#id_apellido").val();
        var correo = $("#id_correo").val();
        var comentario = $("#id_comentario").val();
        var contraseña = $("#id_password").val();
        var confContraseña = $("#id_repeatPassword").val();

        var mensaje = "";

        if (nombre == "") {

            mensaje += "Ingrese Nombre \n";

        }

        if (apellido == "") {

            mensaje += "Ingrese Apellido \n";

        }

        if (correo == "") {
            mensaje += "Ingrese Correo \n";
           
        } else {
           
            var validaFormatoCorreo = caracteresCorreoValido(correo);

            if (validaFormatoCorreo==false) {

                mensaje += "Formato de correo incorrecto, vuelve a ingresarlo!\n";
            }
        }
        if (contraseña == "") {

            mensaje += "Ingrese Contraseña \n";

        }
        if (confContraseña == "") {

            mensaje += "Ingrese Confirmacion Contraseña \n";

        }
        if (contraseña !== confContraseña) {

            mensaje += "Las Contraseñas no son iguales, corrígelas \n";

        }
        if (comentario == "") {

            mensaje += "Ingrese Comentario \n";

        }
        if (mensaje !== "") {

            alert(mensaje);
            return false;

        }
        function caracteresCorreoValido(correo) {


            var caract = new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);

            if (caract.test(correo) == false) {

                return false;
            } else {

                return true;
            }
        }

    });


});


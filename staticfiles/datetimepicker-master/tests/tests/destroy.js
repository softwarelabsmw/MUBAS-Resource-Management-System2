   P  P                                    P  !                   ??  ?  ?  ?I*?              
 ?G     (@?Q??Zb ?   	               <  	              ????@ t z r e s . d l l , - 3 8 2                                                       @ t z r e s . d l l , - 3 8 1                                                   ????    @d?P?????     a???Q??       S I H _ t r a c e _ l o g   C : \ W I N D O W S \ L o g s \ S I H \ S I H . 2 0 2 2 0 9 0 8 . 0 9 0 7 0 2 . 8 5 5 . 1 . e t l   t.contains('xdsoft_datetimepicker')).to.be.true;
            expect(dtp.is(':hidden')).to.be.true;

            $(input).datetimepicker('destroy');
            expect($(input).data('xdsoft_datetimepicker')).to.be.equal(null);

            $(input).trigger('mousedown')
            setTimeout(function () {
                expect(dtp.is(':hidden')).to.be.true;
                done();
            }, 150)
        });
    });
});
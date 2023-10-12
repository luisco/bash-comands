class MetasploitModule < Msf::Auxiliary

    include Msf::Exploit::Remote::HttpClient
    include Msf::Auxiliary::Scanner

      def initialize
           super(
               'Name'          => 'Modulo Hola Mundo',
               'Description'   => 'Este Modulo envia un hello world',
               'Author'      => [ 'Equipo ' ],
               'License'     => MSF_LICENSE
           )
           register_options( [
               Opt::RPORT(90)
           ], self.class)
      end

        def run_host(ip)

            print_status("Trying to Request ")
    
            begin
              res = send_request_cgi({
                'uri'        => '/',
                'method'     => 'GET'
              })
              #print_status(res.body)
              #vprint_good(res)
              return :abort if res.nil?
              return :abort if (res.code == 404)

              if [200, 301, 302].include?(res.code) && res.body.include?('Clase')
                print_good("Prueba superada")
              else
                print_error("Prueba no superada")
                return :abort
              end

              rescue ::Rex::ConnectionError
              vprint_error("Failed to connect to server")
              return :abort
            end
        end
end

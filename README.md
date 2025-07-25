Programa em python para descoberta de host via IP dentro de uma rede.

Funciona como uma consulta de DNS reverso onde ele faz a busca pelo IP e tras o Hostname da máquina. Relacionada ao IP passado.

Como o Script Funciona?
import socket: Importa a biblioteca necessária para operações de rede.

socket.gethostbyaddr(ip): Esta é a função principal. Ela não se conecta diretamente à máquina com o IP fornecido. Em vez disso, ela envia uma consulta a um servidor DNS (geralmente aquele configurado no seu sistema operacional, que pode ser o seu roteador, o DNS do seu provedor de internet ou um DNS público como o do Google 8.8.8.8).

Consulta DNS Reversa : A função pergunta ao servidor DNS: "Qual nome de host corresponde a este endereço IP?". Esse tipo de registro é chamado de PTR(ponteiro).

Tratamento de Erros ( try...except) :

socket.herror: É o erro mais comum que você encontra. Ele significa "Host not found" (Host não encontrado), ou que indica que o servidor DNS consultado não tem nenhum registro de nome para aquele IP.

Outras opções : O bloco captura outros possíveis erros, como um formato de IP inválido.

Limitações e Pontos Importantes
Dependência do DNS : O sucesso deste script para uma máquina desligada depende 100% do registro DNS ainda existente. Em redes domésticas, o seu roteador geralmente atua como um mini servidor DNS e guarda os nomes das máquinas que se conectam a ele via DHCP. Se a concessão de DHCP ( lease) expirar, o roteador pode "esquecer" o nome.

Redes Corporativas x Domésticas : Em redes corporativas com um servidor DNS bem configurado, a chance de sucesso é muito maior, pois os registros são gerenciados de forma mais permanente.

IPs Públicos : Tentar isso com um IP público (como o de um site) geralmente funciona bem, pois os registros DNS para servidores na internet são públicos e permanentes.

Garantia : Não há garantia de que funcionará para uma máquina desligada. Se o registro DNS não existir ou já tiver sido desativado, será impossível obter o nome do host até que a máquina seja conectada novamente e se registre na rede.
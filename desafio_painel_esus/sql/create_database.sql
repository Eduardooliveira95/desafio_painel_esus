USE desafio_esus;

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nascimento VARCHAR(255) NOT NULL,
    cns BIGINT,
    cpf VARCHAR(255),
    unidade VARCHAR(255),
    data_atendimento VARCHAR(255),
    condicao_saude VARCHAR(255)
);

INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-08-10 10:43:39.216577","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-12-19 03:18:47.561698","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-11-06 19:41:54.226493","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-10-14 04:59:44.437488","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-05-13 22:39:26.461473","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-11-26 02:54:47.325142","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2023-12-17 13:40:39.702202","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Elisa Pinto","1978-04-05",75983412655,"320.641.879-87","unidade de saude Maria Alice","2024-04-04 05:50:53.899429","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2023-05-25 06:24:37.640841","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2024-03-14 02:01:15.002655","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2024-01-15 18:33:46.942101","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2023-09-21 07:09:29.409935","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2023-10-20 18:52:56.623456","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2024-04-11 17:16:11.788910","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2024-03-22 16:34:21.708571","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Dr. Rafael Barros","1993-11-22",12394078588,"946.710.253-61","unidade de saude Cecília","2024-02-11 18:54:27.192907","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-08-28 04:39:26.350387","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-11-29 14:18:56.178162","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-11-14 12:38:34.638206","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-11-14 12:38:34.638206","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-12-29 14:55:47.129162","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-12-09 22:02:06.493505","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-10-15 04:14:49.054568","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-11-21 15:46:51.883126","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-10-30 09:00:56.914004","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-07-22 16:16:36.981253","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-06-13 14:43:40.696565","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-12-29 08:45:40.320011","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-02-21 05:01:25.971024","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-02-18 12:34:32.298689","hipertensao");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-02-05 16:42:08.748340","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-01-01 02:53:11.047555","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-09-18 01:13:10.754065","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-01-05 19:56:22.293194","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2024-01-27 03:47:30.166184","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-08-10 01:35:02.802094","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-09-03 02:44:25.571306","diabetes");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-09-02 14:47:42.541029","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-07-12 12:42:06.229384","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-06-05 22:21:48.938671","ferida vascular");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-05-08 06:31:12.184038","dengue");
INSERT INTO Usuario (nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude) VALUES ("Lucas Assis","1979-07-12",52842574760,"907.719.610-92","unidade de saude Maria Alice","2023-12-22 03:33:57.624908","ferida vascular");

UPDATE Usuario
SET data_atendimento = DATE_FORMAT(data_atendimento, '%Y-%m-%d');
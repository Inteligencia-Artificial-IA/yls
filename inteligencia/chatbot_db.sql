CREATE TABLE `preguntas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta` text NOT NULL,
  `respuesta` text NOT NULL,
  `keywords` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `preguntas` (`pregunta`, `respuesta`, `keywords`) VALUES
('¿Cómo estás?', 'Estoy bien, gracias por preguntar. ¿Cómo te encuentras tú?', 'como estas, como te encuentras'),
('¿Cuál es tu nombre?', 'Soy un chatbot diseñado para asistirte con tus consultas. ¿En qué puedo ayudarte hoy?', 'nombre, quien eres, como te llamas'),
('¿Hola?', '¡Hola! ¿En qué puedo ayudarte hoy?', 'hola, saludo, saludos'),
('¿hola?', '¡Hola! Estoy disponible para responder a tus preguntas.', 'hola, saludo, saludos'),
('¿qué tal?', 'Todo está en orden, gracias. ¿Cómo ha sido tu día hasta ahora?', 'que tal, como estas, como va tu dia'),
('¿que tal?', 'Estoy bien, gracias por preguntar. ¿Cómo te va a ti?', 'que tal, como estas, como te va'),
('¿cómo te va?', 'Me va muy bien, gracias. ¿Y cómo te va a ti?', 'como te va, como estas'),
('¿qué haces?', 'Estoy aquí para ayudarte con cualquier consulta que tengas. ¿En qué puedo asistirte?', 'que haces, en que estas, que estas haciendo'),
('¿Cuáles son los requisitos para las prácticas pre profesionales?', 'Los requisitos para las Prácticas Pre Profesionales varían según el plan de estudios vigente. Te recomiendo consultar los planes de estudios correspondientes a los años 2013, 2016, y 2020 para más detalles.', 'requisitos, practicas pre profesionales, practicas'),
('¿Cómo solicito el reconocimiento del Ejercicio Pre Profesional?', 'Para solicitar el reconocimiento del Ejercicio Pre Profesional, debes hacerlo a través de la mesa de partes virtual, adjuntando el recibo de pago correspondiente, el informe final, y la carta de presentación emitida por la empresa donde realizaste las prácticas.', 'solicitar, reconocimiento, ejercicio pre profesional, solicitar reconocimiento'),
('¿Dónde puedo encontrar más información sobre las prácticas?', 'Puedes encontrar más información visitando el sitio web oficial de la universidad en el siguiente enlace: <a href="https://sites.google.com/view/pppsistemasuac/inicio?authuser=0" target="_blank">Sitio oficial de la UAC</a>.', 'informacion, practicas, sitio web, oficial'),
('¿Qué documentos necesito para el reconocimiento de prácticas?', 'Para el reconocimiento de prácticas, necesitas presentar el recibo de pago (código C33290001), el informe final de tus actividades, y la carta de presentación emitida por la empresa.', 'documentos, reconocimiento practicas, practicas, documentos necesarios'),
('¿Cómo puedo unirme al grupo de WhatsApp?', 'Para unirte al grupo de WhatsApp, puedes seguir este enlace: <a href="https://chat.whatsapp.com/EQEBN6eAhOc6W3CVKULsed" target="_blank">Unirme al grupo de WhatsApp</a>.', 'unirme, grupo, whatsapp, grupo whatsapp, chat'),
('¿Cuál es el horario de atención para ING 413?', 'El horario de atención para el curso ING 413 es: Lunes y Martes de 2:00pm a 4:00pm, y Jueves y Viernes de 7:00am a 9:00am.', 'horario, atencion, ing 413, curso');



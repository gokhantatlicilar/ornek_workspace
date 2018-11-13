def sendAndReceive(self, content):
  logger.info('Sending {0}'.format(content))
  self.ser.write(content + '\r')
  self.ser.flush();
  response = self.ser.readline() # Currently stops reading on timeout...
  if self.isErr(response):
    logger.error(response)
    return None
  else:
    return response

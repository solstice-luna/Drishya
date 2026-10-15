import { Body, Controller, Post, UseGuards } from '@nestjs/common';
import { RecognitionEventsService } from './recognition-events.service.js';
import { CreateRecognitionEventDto } from './dto/create-recognition-event.dto.js';
import { AiServiceTokenGuard } from './ai-service-token.guard.js';

@Controller('api/v1/recognition-events')
@UseGuards(AiServiceTokenGuard)
export class RecognitionEventsController {
  constructor(
    private readonly recognitionEventsService: RecognitionEventsService,
  ) {}

  @Post()
  receive(@Body() event: CreateRecognitionEventDto) {
    return this.recognitionEventsService.receive(event);
  }
}

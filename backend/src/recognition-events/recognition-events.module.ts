import { Module } from '@nestjs/common';
import { RecognitionEventsController } from './recognition-events.controller.js';
import { AiServiceTokenGuard } from './ai-service-token.guard.js';
import { RecognitionEventsService } from './recognition-events.service.js';

@Module({
  controllers: [RecognitionEventsController],
  providers: [AiServiceTokenGuard, RecognitionEventsService],
})
export class RecognitionEventsModule {}

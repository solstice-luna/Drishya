import { Module } from '@nestjs/common';
import { AppController } from './app.controller.js';
import { AppService } from './app.service.js';
import { RecognitionEventsModule } from './recognition-events/recognition-events.module.js';

@Module({
  imports: [RecognitionEventsModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

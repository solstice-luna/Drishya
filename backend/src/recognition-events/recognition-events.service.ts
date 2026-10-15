import { Injectable } from '@nestjs/common';
import { CreateRecognitionEventDto } from './dto/create-recognition-event.dto.js';

@Injectable()
export class RecognitionEventsService {
  receive(event: CreateRecognitionEventDto) {
    // Temporary: persistence will be added in a later milestone.
    return {
      success: true,
      message: 'Recognition event received.',
      event,
    };
  }
}

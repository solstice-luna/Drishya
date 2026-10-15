import {
  CanActivate,
  ExecutionContext,
  Injectable,
  UnauthorizedException,
} from '@nestjs/common';
import { timingSafeEqual } from 'node:crypto';
import type { Request } from 'express';

@Injectable()
export class AiServiceTokenGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest<Request>();
    const receivedToken = request.header('x-ai-service-token');
    const configuredToken = process.env.AI_SERVICE_TOKEN;

    if (!receivedToken || !configuredToken) {
      throw new UnauthorizedException('Invalid AI service token.');
    }

    const received = Buffer.from(receivedToken);
    const configured = Buffer.from(configuredToken);

    if (
      received.length !== configured.length ||
      !timingSafeEqual(received, configured)
    ) {
      throw new UnauthorizedException('Invalid AI service token.');
    }

    return true;
  }
}

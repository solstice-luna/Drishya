import { IsIn, IsISO8601, IsString, MaxLength, Matches } from 'class-validator';

export class CreateRecognitionEventDto {
  @IsIn(['student', 'teacher'])
  person_type: 'student' | 'teacher';

  @IsString()
  @MaxLength(100)
  @Matches(/^[a-zA-Z0-9_-]+$/)
  person_identifier: string;

  @IsString()
  @MaxLength(100)
  @Matches(/^[a-zA-Z0-9_-]+$/)
  camera: string;

  @IsISO8601({ strict: true })
  recognized_at: string;
}

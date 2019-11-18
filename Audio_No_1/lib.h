/***************************************************************************
○ ファイル名：read_write.c
○ 内容：読み込み，書き込み, メモリ確保等の関数群

Copyright @ ASPL all rights reserved.
***************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/***************************************************************************
○ 関数名：short* Read_Raw_File_Short( char *fname, int *dtSize )
○ 内容：RAW形式の音源(fname)から量子化ビット16bitで抽出
         サンプル数は*dtSizeに格納
○ 引数：char *fname：入力ファイル名
       ：int *dtSize：入力ファイルのサンプル数を格納する変数のアドレス
○ 戻り値：入力ファイルの標本データの先頭アドレス
***************************************************************************/
short* Read_Raw_File_Short( char *fname, int *dtSize ){

	short *data;

	FILE *fp;

	// ファイルオープン
	if( ( fp = fopen( fname, "rb" ) ) == NULL ){
		printf("Read_Raw_File_Short() : FILE [%s] ERROR\n", fname);
		exit( -1 );
	}

	// 標本数の取得
	fseek( fp, 0, SEEK_END );
	*dtSize = ftell( fp ) / sizeof( short );
	fseek( fp, 0, SEEK_SET );

	// 標本数分のメモリ確保
	if( ( data = ( short* )malloc( sizeof( short ) * ( *dtSize ) ) ) == NULL ){
		printf("Read_Raw_File_Short() : MALLOC ERROR\n");
		exit( -1 );
	}

	// 標本データの格納
	if( fread( data, sizeof( short ), *dtSize, fp ) < *dtSize ){
		printf("Read_Raw_File_Short() : DATA READ ERROR\n");
		exit( -1 );
	}

	// ファイルクローズ
	fclose( fp );

	return( data );
}

/***************************************************************************
○ 関数名：void Write_Raw_File_Short( short *data, char *fname, int dtSize )
○ 内容：*dataから量子化ビット16bitの標本値をdtSize個分
         RAW形式の音源(fname)に格納
○ 引数：short *data：出力する標本データ
       ：char *fname：出力ファイル名
       ：int dtSize：出力ファイルのサンプル数
○ 戻り値：なし
***************************************************************************/
void Write_Raw_File_Short( short *data, char *fname, int dtSize ){

	FILE *fp;

	// ファイルオープン
	if( ( fp = fopen( fname, "wb" ) ) == NULL ){
		printf("Write_Raw_File_Short() : FILE [%s] ERROR\n", fname);
		exit( -1 );
	}

	// データ書き込み
	if( fwrite( data, sizeof( short ), dtSize, fp ) < dtSize ){
		printf("Write_Raw_File_Short() : DATA WRITE ERROR\n");
		exit( -1 );
	}

	// ファイルクローズ
	fclose( fp );
}

/***************************************************************************
○ 関数名：double* Read_Raw_File_Double( char *fname, int *dtSize )
○ 内容：RAW形式の音源(fname)から量子化ビット64bitで抽出
         サンプル数は*dtSizeに格納
○ 引数：char *fname：入力ファイル名
       ：int *dtSize：入力ファイルのサンプル数を格納する変数のアドレス
○ 戻り値：入力ファイルの標本データの先頭アドレス
***************************************************************************/
double* Read_Raw_File_Double( char *fname, int *dtSize ){

	double *data;

	FILE *fp;

	// ファイルオープン
	if( ( fp = fopen( fname, "rb" ) ) == NULL ){
		printf("Read_Raw_File_Short() : FILE [%s] ERROR\n", fname);
		exit( -1 );
	}

	// 標本数の取得
	fseek( fp, 0, SEEK_END );
	*dtSize = ftell( fp ) / sizeof( double );
	fseek( fp, 0, SEEK_SET );

	// 標本数分のメモリ確保
	if( ( data = ( double* )malloc( sizeof( double ) * ( *dtSize ) ) ) == NULL ){
		printf("Read_Raw_File_Short() : MALLOC ERROR\n");
		exit( -1 );
	}

	// 標本データの格納
	if( fread( data, sizeof( double ), *dtSize, fp ) < *dtSize ){
		printf("Read_Raw_File_Short() : DATA READ ERROR\n");
		exit( -1 );
	}

	// ファイルクローズ
	fclose( fp );

	return( data );
}

/***************************************************************************
○ 関数名：void Write_Raw_File_Double( double *data, char *fname, int dtSize )
○ 内容：*dataから量子化ビット64bitの標本値をdtSize個分
         RAW形式の音源(fname)に格納
○ 引数：double *data：出力する標本データ
       ：char *fname：出力ファイル名
       ：int dtSize：出力ファイルのサンプル数
○ 戻り値：なし
***************************************************************************/
void Write_Raw_File_Double( double *data, char *fname, int dtSize ){

	FILE *fp;

	// ファイルオープン
	if( ( fp = fopen( fname, "wb" ) ) == NULL ){
		printf("Write_Raw_File_Short() : FILE [%s] ERROR\n", fname);
		exit( -1 );
	}

	// データ書き込み
	if( fwrite( data, sizeof( double ), dtSize, fp ) < dtSize ){
		printf("Write_Raw_File_Short() : DATA WRITE ERROR\n");
		exit( -1 );
	}

	// ファイルクローズ
	fclose( fp );
}

/***************************************************************************
○ 関数名：double* Memory_Double( int dtSize )
○ 内容：double型のメモリをdtSize個確保する
○ 引数：int dtSize：入力ファイルのサンプル数
○ 戻り値：確保したメモリの先頭アドレス
***************************************************************************/
double* Memory_Double( int dtSize ){

	double *data;

	// メモリ確保
	if( ( data = ( double * )malloc( sizeof( double ) * dtSize ) ) == NULL ){
		fprintf( stderr, "Memory_Double() : MALLOC ERROR\n");
		exit( -1 );
	}

	return( data );
}

/***************************************************************************
○ 関数名：short* Memory_Short( int dtSize )
○ 内容：short型のメモリをdtSize個確保する
○ 引数：int dtSize：入力ファイルのサンプル数
○ 戻り値：確保したメモリの先頭アドレス
***************************************************************************/
short* Memory_Short( int dtSize ){

	short *data;

	// メモリ確保
	if( ( data = ( short * )malloc( sizeof( short ) * dtSize ) ) == NULL ){
		fprintf( stderr, "Memory_Short() : MALLOC ERROR\n");
		exit( -1 );
	}

	return( data );
}


/***************************************************************************
○ 関数名：void DFT(int N, double D[], double Xr[], double Xi[])
○ 内容：入力信号D[]をフーリエ点数Nでフーリエ変換した結果を
         実部Xr[], 虚部Xi[]に格納する
○ 引数：int N：フーリエ点数
         double D[]：入力信号
         double Xr[]：フーリエ変換結果（実部）
         double Xi[]：フーリエ変換結果（虚部）
○ 戻り値：なし
***************************************************************************/
void DFT(int N, double D[], double Xr[], double Xi[]){

  int k, n;              // ループカウンタ
  double er, ei;         // 実部・虚部

  double w;              // 各周波数
	double pai=3.1415926;  // 円周率

	// フーリエ変換
  for( k = 0; k < N; k++ ){

    Xr[ k ] = Xi[ k ] = 0.0;

    for( n = 0; n < N; n++ ){

  		w = 2 * pai * k * n / N;
			er = D[ n ] * cos( w );
			ei = D[ n ] * sin( -w );

      Xr[ k ] += er / N;
      Xi[ k ] += ei / N;
    }
  }
}

﻿//  ---------------------------------------------------------------------------------
//  Copyright (c) Microsoft Open Technologies, Inc.  All rights reserved.
// 
//  The MIT License (MIT)
// 
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to deal
//  in the Software without restriction, including without limitation the rights
//  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//  copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
// 
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
// 
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
//  THE SOFTWARE.
//  ---------------------------------------------------------------------------------

namespace Microsoft.ConnectTheDots.Common
{
    using NLog;

    public class NLogEventLogger : ILogger
    {
        #region Singleton implementation

        private static readonly object  _syncRoot = new object( );

        //--//

        private static ILogger          _NLogEventLoggerInstance;
        private static NLog.Logger      _NLog;

        //--//

        public static ILogger Instance
        {
            get
            {
                if( _NLogEventLoggerInstance == null )
                {
                    lock( _syncRoot )
                    {
                        if( _NLogEventLoggerInstance == null )
                        {
                            _NLogEventLoggerInstance = new NLogEventLogger( );
                        }
                    }
                }

                return _NLogEventLoggerInstance;
            }
        }

        private NLogEventLogger( )
        {
            _NLog = LogManager.GetCurrentClassLogger( );
        }

        #endregion

        public void Flush( )
        {
            LogManager.Flush( );
        }

        public void LogError( string logMessage )
        {
            _NLog.Error( logMessage );
        }

        public void LogInfo( string logMessage )
        {
            _NLog.Info( logMessage );
        }
    }
}

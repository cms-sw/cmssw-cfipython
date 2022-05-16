import FWCore.ParameterSet.Config as cms

TestService = cms.Service('TestService',
  printTestMessageLoggerErrors = cms.untracked.bool(False)
)

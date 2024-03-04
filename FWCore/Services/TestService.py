import FWCore.ParameterSet.Config as cms

def TestService(**kwargs):
  mod = cms.Service('TestService',
    printTestMessageLoggerErrors = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

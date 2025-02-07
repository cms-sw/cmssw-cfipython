import FWCore.ParameterSet.Config as cms

def TestService(*args, **kwargs):
  mod = cms.Service('TestService',
    printTestMessageLoggerErrors = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

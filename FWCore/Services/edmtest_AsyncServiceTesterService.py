import FWCore.ParameterSet.Config as cms

def edmtest_AsyncServiceTesterService(*args, **kwargs):
  mod = cms.Service('edmtest::AsyncServiceTesterService',
    watchEarlyTermination = cms.bool(False),
    watchStreamEndRun = cms.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

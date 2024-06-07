import FWCore.ParameterSet.Config as cms

def edmtest_AsyncServiceTesterService(**kwargs):
  mod = cms.Service('edmtest::AsyncServiceTesterService',
    watchEarlyTermination = cms.bool(False),
    watchStreamEndRun = cms.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

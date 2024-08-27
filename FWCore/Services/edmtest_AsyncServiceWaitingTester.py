import FWCore.ParameterSet.Config as cms

def edmtest_AsyncServiceWaitingTester(**kwargs):
  mod = cms.EDProducer('edmtest::AsyncServiceWaitingTester',
    throwingStream = cms.required.untracked.uint32,
    waitEarlyTermination = cms.untracked.bool(False),
    waitStreamEndRun = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

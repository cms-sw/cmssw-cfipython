import FWCore.ParameterSet.Config as cms

def edmtest_AsyncServiceWaitingTester(*args, **kwargs):
  mod = cms.EDProducer('edmtest::AsyncServiceWaitingTester',
    throwingStream = cms.required.untracked.uint32,
    waitEarlyTermination = cms.untracked.bool(False),
    waitStreamEndRun = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ExceptionThrowingProducer(**kwargs):
  mod = cms.EDProducer('ExceptionThrowingProducer',
    verbose = cms.untracked.bool(False),
    eventIDThrowOnEvent = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalBeginRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalBeginLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalEndRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalEndLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamBeginRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamBeginLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamEndRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamEndLumi = cms.untracked.EventID(0, 0, 0),
    expectedStreamBeginLumi = cms.untracked.uint32(4294967295),
    expectedOffsetNoStreamEndLumi = cms.untracked.uint32(0),
    expectedGlobalBeginLumi = cms.untracked.uint32(0),
    expectedOffsetNoGlobalEndLumi = cms.untracked.uint32(0),
    expectedOffsetNoWriteLumi = cms.untracked.uint32(0),
    expectedStreamBeginRun = cms.untracked.uint32(4294967295),
    expectedOffsetNoStreamEndRun = cms.untracked.uint32(0),
    expectedGlobalBeginRun = cms.untracked.uint32(0),
    expectedOffsetNoGlobalEndRun = cms.untracked.uint32(0),
    expectedOffsetNoWriteRun = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

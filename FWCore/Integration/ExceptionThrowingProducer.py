import FWCore.ParameterSet.Config as cms

def ExceptionThrowingProducer(*args, **kwargs):
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
    throwInBeginJob = cms.untracked.bool(False),
    throwInBeginStream = cms.untracked.bool(False),
    throwInBeginProcessBlock = cms.untracked.bool(False),
    throwInEndProcessBlock = cms.untracked.bool(False),
    throwInEndStream = cms.untracked.bool(False),
    throwInEndJob = cms.untracked.bool(False),
    expectedNBeginJob = cms.untracked.uint32(1),
    expectedNBeginStream = cms.untracked.uint32(4),
    expectedNBeginProcessBlock = cms.untracked.uint32(1),
    expectedNEndProcessBlock = cms.untracked.uint32(1),
    expectedNEndStream = cms.untracked.uint32(4),
    expectedNEndJob = cms.untracked.uint32(1),
    expectNoRunsProcessed = cms.untracked.bool(False),
    expectedOffsetNoEndJob = cms.untracked.uint32(0),
    expectedOffsetNoEndStream = cms.untracked.uint32(0),
    expectedOffsetNoEndProcessBlock = cms.untracked.uint32(0),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

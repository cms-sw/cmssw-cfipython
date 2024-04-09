import FWCore.ParameterSet.Config as cms

def ExceptionThrowingProducer(**kwargs):
  mod = cms.EDProducer('ExceptionThrowingProducer',
    eventIDThrowOnEvent = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalBeginRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalBeginLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalEndRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnGlobalEndLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamBeginRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamBeginLumi = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamEndRun = cms.untracked.EventID(0, 0, 0),
    eventIDThrowOnStreamEndLumi = cms.untracked.EventID(0, 0, 0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
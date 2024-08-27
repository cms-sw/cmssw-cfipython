import FWCore.ParameterSet.Config as cms

def TTStubBuilder_Phase2TrackerDigi_(**kwargs):
  mod = cms.EDProducer('TTStubBuilder_Phase2TrackerDigi_',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

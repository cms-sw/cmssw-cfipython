import FWCore.ParameterSet.Config as cms

def Phase2TrackerValidateDigi(**kwargs):
  mod = cms.EDProducer('Phase2TrackerValidateDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
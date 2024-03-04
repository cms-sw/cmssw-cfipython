import FWCore.ParameterSet.Config as cms

def TrackerHitProducer(**kwargs):
  mod = cms.EDProducer('TrackerHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

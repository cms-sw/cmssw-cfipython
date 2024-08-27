import FWCore.ParameterSet.Config as cms

def TauValTrackViewCleaner(**kwargs):
  mod = cms.EDProducer('TauValTrackViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

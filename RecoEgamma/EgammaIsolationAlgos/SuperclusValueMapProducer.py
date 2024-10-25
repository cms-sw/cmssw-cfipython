import FWCore.ParameterSet.Config as cms

def SuperclusValueMapProducer(**kwargs):
  mod = cms.EDProducer('SuperclusValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

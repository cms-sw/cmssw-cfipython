import FWCore.ParameterSet.Config as cms

def PFTrackProducer(**kwargs):
  mod = cms.EDProducer('PFTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

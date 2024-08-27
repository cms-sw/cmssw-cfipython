import FWCore.ParameterSet.Config as cms

def PPSSimTrackProducer(**kwargs):
  mod = cms.EDProducer('PPSSimTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

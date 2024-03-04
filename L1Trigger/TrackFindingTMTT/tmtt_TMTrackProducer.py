import FWCore.ParameterSet.Config as cms

def tmtt_TMTrackProducer(**kwargs):
  mod = cms.EDProducer('tmtt::TMTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

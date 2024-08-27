import FWCore.ParameterSet.Config as cms

def IsFromLostTrackMapProducer(**kwargs):
  mod = cms.EDProducer('IsFromLostTrackMapProducer',
    srcIsoTracks = cms.required.InputTag,
    lostTracks = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

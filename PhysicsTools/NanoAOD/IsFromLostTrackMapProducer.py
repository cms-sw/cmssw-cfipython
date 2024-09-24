import FWCore.ParameterSet.Config as cms

def IsFromLostTrackMapProducer(*args, **kwargs):
  mod = cms.EDProducer('IsFromLostTrackMapProducer',
    srcIsoTracks = cms.required.InputTag,
    lostTracks = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

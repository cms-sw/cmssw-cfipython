import FWCore.ParameterSet.Config as cms

def tmtt_TMTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('tmtt::TMTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

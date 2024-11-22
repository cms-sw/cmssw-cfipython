import FWCore.ParameterSet.Config as cms

def RecoTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('RecoTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

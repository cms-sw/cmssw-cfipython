import FWCore.ParameterSet.Config as cms

def RecoTrackViewRefSelector(*args, **kwargs):
  mod = cms.EDProducer('RecoTrackViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

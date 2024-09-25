import FWCore.ParameterSet.Config as cms

def RecoTrackRefSelector(*args, **kwargs):
  mod = cms.EDProducer('RecoTrackRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

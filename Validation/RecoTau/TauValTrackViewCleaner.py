import FWCore.ParameterSet.Config as cms

def TauValTrackViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValTrackViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

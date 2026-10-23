import FWCore.ParameterSet.Config as cms

def TrackerHitProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackerHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

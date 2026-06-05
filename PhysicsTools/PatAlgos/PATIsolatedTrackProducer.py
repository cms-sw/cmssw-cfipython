import FWCore.ParameterSet.Config as cms

def PATIsolatedTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('PATIsolatedTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

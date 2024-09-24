import FWCore.ParameterSet.Config as cms

def pfTracksProducer(*args, **kwargs):
  mod = cms.EDProducer('pfTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ShallowSimTracksProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowSimTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

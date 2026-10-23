import FWCore.ParameterSet.Config as cms

def ShallowTracksProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowTracksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

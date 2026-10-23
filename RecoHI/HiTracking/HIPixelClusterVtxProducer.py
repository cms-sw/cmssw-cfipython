import FWCore.ParameterSet.Config as cms

def HIPixelClusterVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('HIPixelClusterVtxProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TopBottomClusterInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TopBottomClusterInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

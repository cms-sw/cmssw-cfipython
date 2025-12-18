import FWCore.ParameterSet.Config as cms

def PreshowerClusterShapeProducer(*args, **kwargs):
  mod = cms.EDProducer('PreshowerClusterShapeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

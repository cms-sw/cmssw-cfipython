import FWCore.ParameterSet.Config as cms

def PreshowerClusterShapeProducer(**kwargs):
  mod = cms.EDProducer('PreshowerClusterShapeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

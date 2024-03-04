import FWCore.ParameterSet.Config as cms

def MtdSimLayerClusterToTPAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MtdSimLayerClusterToTPAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

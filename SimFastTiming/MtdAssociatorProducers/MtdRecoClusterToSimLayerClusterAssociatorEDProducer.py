import FWCore.ParameterSet.Config as cms

def MtdRecoClusterToSimLayerClusterAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

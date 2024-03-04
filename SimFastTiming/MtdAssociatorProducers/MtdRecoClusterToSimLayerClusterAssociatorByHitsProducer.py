import FWCore.ParameterSet.Config as cms

def MtdRecoClusterToSimLayerClusterAssociatorByHitsProducer(**kwargs):
  mod = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorByHitsProducer',
    energyCut = cms.double(5),
    timeCut = cms.double(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

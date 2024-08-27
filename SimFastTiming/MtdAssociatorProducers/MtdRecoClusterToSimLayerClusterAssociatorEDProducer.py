import FWCore.ParameterSet.Config as cms

def MtdRecoClusterToSimLayerClusterAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorEDProducer',
    associator = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociatorByHits'),
    mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
    btlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
    etlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

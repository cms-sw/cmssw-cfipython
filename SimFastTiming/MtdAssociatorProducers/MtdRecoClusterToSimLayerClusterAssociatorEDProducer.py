import FWCore.ParameterSet.Config as cms

def MtdRecoClusterToSimLayerClusterAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorEDProducer',
    associator = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociatorByHits'),
    mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
    btlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
    etlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

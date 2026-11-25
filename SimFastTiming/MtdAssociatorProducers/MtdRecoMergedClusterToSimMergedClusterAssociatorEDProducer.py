import FWCore.ParameterSet.Config as cms

def MtdRecoMergedClusterToSimMergedClusterAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdRecoMergedClusterToSimMergedClusterAssociatorEDProducer',
    associator = cms.InputTag('mtdRecoMergedClusterToSimMergedClusterAssociatorByHits'),
    mtdSimMergedClustersTag = cms.InputTag('mtdSimMergedClusterProducer'),
    btlRecoClustersTag = cms.InputTag('mtdMergedClusters', 'FTLBarrel'),
    etlRecoClustersTag = cms.InputTag('mtdMergedClusters', 'FTLEndcap'),
    etlConstituentsTag = cms.InputTag('mtdMergedClusters', 'FTLEndcapConstituents'),
    btlConstituentsTag = cms.InputTag('mtdMergedClusters', 'FTLBarrelConstituents'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

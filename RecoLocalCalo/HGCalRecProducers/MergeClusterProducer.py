import FWCore.ParameterSet.Config as cms

def MergeClusterProducer(**kwargs):
  mod = cms.EDProducer('MergeClusterProducer',
    layerClustersEE = cms.InputTag('hgcalLayerClustersEE'),
    layerClustersHSi = cms.InputTag('hgcalLayerClustersHSi'),
    layerClustersHSci = cms.InputTag('hgcalLayerClustersHSci'),
    time_layerclustersEE = cms.InputTag('hgcalLayerClustersEE', 'timeLayerCluster'),
    time_layerclustersHSi = cms.InputTag('hgcalLayerClustersHSi', 'timeLayerCluster'),
    time_layerclustersHSci = cms.InputTag('hgcalLayerClustersHSci', 'timeLayerCluster'),
    timeClname = cms.string('timeLayerCluster'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

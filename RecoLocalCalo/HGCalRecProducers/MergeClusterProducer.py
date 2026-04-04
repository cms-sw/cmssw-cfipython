import FWCore.ParameterSet.Config as cms

def MergeClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('MergeClusterProducer',
    layerClusters = cms.VInputTag(
      'hgcalLayerClustersEE',
      'hgcalLayerClustersHSi',
      'hgcalLayerClustersHSci'
    ),
    time_layerclusters = cms.VInputTag(
      'hgcalLayerClustersEE:timeLayerCluster',
      'hgcalLayerClustersHSi:timeLayerCluster',
      'hgcalLayerClustersHSci:timeLayerCluster'
    ),
    timeClname = cms.string('timeLayerCluster'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

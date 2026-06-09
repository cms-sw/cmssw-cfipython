import FWCore.ParameterSet.Config as cms

def LayerClustersExtraTableProducer(*args, **kwargs):
  mod = cms.EDProducer('LayerClustersExtraTableProducer',
    skipNonExistingSrc = cms.bool(False),
    tableName = cms.string('hltMergeLayerClusters'),
    time_layerclusters = cms.InputTag('hltMergeLayerClusters', 'timeLayerCluster'),
    precision = cms.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

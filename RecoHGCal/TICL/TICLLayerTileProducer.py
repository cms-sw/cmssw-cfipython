import FWCore.ParameterSet.Config as cms

def TICLLayerTileProducer(*args, **kwargs):
  mod = cms.EDProducer('TICLLayerTileProducer',
    detector = cms.string('HGCAL'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_HFNose_clusters = cms.InputTag('hgcalLayerClustersHFNose'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

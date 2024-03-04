import FWCore.ParameterSet.Config as cms

def TICLLayerTileProducer(**kwargs):
  mod = cms.EDProducer('TICLLayerTileProducer',
    detector = cms.string('HGCAL'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_HFNose_clusters = cms.InputTag('hgcalLayerClustersHFNose'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def AllLayerClusterToTracksterAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllLayerClusterToTracksterAssociatorsProducer',
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersCLUE3DHigh',
      'ticlTrackstersLinks',
      'ticlCandidate'
    ),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

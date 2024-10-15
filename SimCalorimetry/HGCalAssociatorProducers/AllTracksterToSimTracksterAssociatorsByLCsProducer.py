import FWCore.ParameterSet.Config as cms

def AllTracksterToSimTracksterAssociatorsByLCsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllTracksterToSimTracksterAssociatorsByLCsProducer',
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersCLUE3DHigh',
      'ticlTrackstersLinks'
    ),
    simTracksterCollections = cms.VInputTag(
      'ticlSimTracksters',
      'ticlSimTracksters:fromCPs'
    ),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

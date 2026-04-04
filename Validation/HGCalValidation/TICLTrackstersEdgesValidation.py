import FWCore.ParameterSet.Config as cms

def TICLTrackstersEdgesValidation(*args, **kwargs):
  mod = cms.EDProducer('TICLTrackstersEdgesValidation',
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersTrk',
      'ticlTrackstersTrkEM',
      'ticlTrackstersEM',
      'ticlTrackstersHAD',
      'ticlTrackstersMerge'
    ),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    ticlSeedingGlobal = cms.InputTag('ticlSeedingGlobal'),
    ticlSeedingTrk = cms.InputTag('ticlSeedingTrk'),
    folder = cms.string('HGCAL/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

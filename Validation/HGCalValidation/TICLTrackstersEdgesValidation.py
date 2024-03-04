import FWCore.ParameterSet.Config as cms

def TICLTrackstersEdgesValidation(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

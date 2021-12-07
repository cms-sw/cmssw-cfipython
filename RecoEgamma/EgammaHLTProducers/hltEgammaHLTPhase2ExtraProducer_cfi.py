import FWCore.ParameterSet.Config as cms

hltEgammaHLTPhase2ExtraProducer = cms.EDProducer('EgammaHLTPhase2ExtraProducer',
  egTrigObjs = cms.InputTag('hltEgammaHLTExtra'),
  l1Trks = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  trkParts = cms.InputTag('mix', 'MergedTrackTruth'),
  l1TrkToTrkPartMap = cms.InputTag('TTTrackAssociatorFromPixelDigis', 'Level1TTTracks'),
  hgcalLayerClusters = cms.InputTag('hgcalLayerClusters'),
  hgcalLayerClustersTime = cms.InputTag('hgcalLayerClusters', 'timeLayerCluster'),
  minPtToSaveHits = cms.double(0),
  saveHitsPlusPi = cms.bool(True),
  saveHitsPlusHalfPi = cms.bool(True),
  recHitCountThresholds = cms.vdouble(
    0,
    0.5,
    1,
    1.5,
    2
  ),
  hgcal = cms.VPSet(
    cms.PSet(
      label = cms.string('HGCEERecHits'),
      src = cms.InputTag('HGCalRecHit', 'HGCEERecHits')
    ),
    cms.PSet(
      label = cms.string('HGCHEFRecHits'),
      src = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits')
    ),
    cms.PSet(
      label = cms.string('HGCHEBRecHits'),
      src = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)

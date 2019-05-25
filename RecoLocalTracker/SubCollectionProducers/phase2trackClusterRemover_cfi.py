import FWCore.ParameterSet.Config as cms

phase2trackClusterRemover = cms.EDProducer('TrackClusterRemoverPhase2',
  trajectories = cms.InputTag(''),
  trackClassifier = cms.InputTag('', 'QualityMasks'),
  phase2pixelClusters = cms.InputTag('siPixelClusters'),
  phase2OTClusters = cms.InputTag('siPhase2Clusters'),
  oldClusterRemovalInfo = cms.InputTag(''),
  TrackQuality = cms.string('highPurity'),
  maxChi2 = cms.double(30),
  minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
  overrideTrkQuals = cms.InputTag('')
)

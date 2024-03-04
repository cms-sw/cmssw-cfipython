import FWCore.ParameterSet.Config as cms

def TrackClusterRemover(**kwargs):
  mod = cms.EDProducer('TrackClusterRemover',
    trajectories = cms.InputTag(''),
    trackClassifier = cms.InputTag('', 'QualityMasks'),
    pixelClusters = cms.InputTag('siPixelClusters'),
    stripClusters = cms.InputTag('siStripClusters'),
    oldClusterRemovalInfo = cms.InputTag(''),
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(30),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    overrideTrkQuals = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

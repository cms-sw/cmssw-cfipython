import FWCore.ParameterSet.Config as cms

def MeasurementTrackerEventProducer(**kwargs):
  mod = cms.EDProducer('MeasurementTrackerEventProducer',
    measurementTracker = cms.string(''),
    skipClusters = cms.InputTag(''),
    pixelClusterProducer = cms.string('siPixelClusters'),
    stripClusterProducer = cms.string('siStripClusters'),
    Phase2TrackerCluster1DProducer = cms.string(''),
    vectorHits = cms.InputTag(''),
    vectorHitsRej = cms.InputTag(''),
    inactivePixelDetectorLabels = cms.VInputTag('siPixelDigis'),
    badPixelFEDChannelCollectionLabels = cms.VInputTag(),
    pixelCablingMapLabel = cms.string(''),
    inactiveStripDetectorLabels = cms.VInputTag('siStripDigis'),
    switchOffPixelsIfEmpty = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

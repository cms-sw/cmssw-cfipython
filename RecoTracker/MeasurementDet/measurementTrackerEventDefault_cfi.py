import FWCore.ParameterSet.Config as cms

measurementTrackerEventDefault = cms.EDProducer('MeasurementTrackerEventProducer',
  measurementTracker = cms.string(''),
  skipClusters = cms.InputTag(''),
  pixelClusterProducer = cms.string('siPixelClusters'),
  stripClusterProducer = cms.string('siStripClusters'),
  Phase2TrackerCluster1DProducer = cms.string(''),
  inactivePixelDetectorLabels = cms.VInputTag('siPixelDigis'),
  badPixelFEDChannelCollectionLabels = cms.VInputTag(),
  pixelCablingMapLabel = cms.string(''),
  inactiveStripDetectorLabels = cms.VInputTag('siStripDigis'),
  switchOffPixelsIfEmpty = cms.bool(True)
)

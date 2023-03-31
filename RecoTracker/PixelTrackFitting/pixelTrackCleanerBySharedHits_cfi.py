import FWCore.ParameterSet.Config as cms

pixelTrackCleanerBySharedHits = cms.ESProducer('PixelTrackCleanerBySharedHitsESProducer',
  ComponentName = cms.string('pixelTrackCleanerBySharedHits'),
  useQuadrupletAlgo = cms.bool(False),
  appendToDataLabel = cms.string('')
)

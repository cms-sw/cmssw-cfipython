import FWCore.ParameterSet.Config as cms

tkTransientTrackingRecHitBuilderESProducer = cms.ESProducer('TkTransientTrackingRecHitBuilderESProducer',
  ComponentName = cms.string('Fake'),
  ComputeCoarseLocalPositionFromDisk = cms.bool(False),
  StripCPE = cms.string('Fake'),
  PixelCPE = cms.string('Fake'),
  Matcher = cms.string('Fake'),
  Phase2StripCPE = cms.string(''),
  appendToDataLabel = cms.string('')
)

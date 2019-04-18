import FWCore.ParameterSet.Config as cms

trackingParticleConversionSelector = cms.EDProducer('TrackingParticleConversionSelector',
  src = cms.InputTag('mix', 'MergedTrackTruth')
)

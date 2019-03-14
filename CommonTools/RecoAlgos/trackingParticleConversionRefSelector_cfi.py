import FWCore.ParameterSet.Config as cms

trackingParticleConversionRefSelector = cms.EDProducer('TrackingParticleConversionRefSelector',
  src = cms.InputTag('mix', 'MergedTrackTruth')
)

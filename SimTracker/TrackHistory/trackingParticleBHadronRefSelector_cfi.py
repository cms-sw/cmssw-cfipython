import FWCore.ParameterSet.Config as cms

trackingParticleBHadronRefSelector = cms.EDProducer('TrackingParticleBHadronRefSelector',
  src = cms.InputTag('mix', 'MergedTrackTruth')
)

import FWCore.ParameterSet.Config as cms

trackingParticleBHadronRefSelectorDefault = cms.EDProducer('TrackingParticleBHadronRefSelector',
  src = cms.InputTag('mix', 'MergedTrackTruth')
)

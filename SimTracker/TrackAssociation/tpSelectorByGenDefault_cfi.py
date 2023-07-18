import FWCore.ParameterSet.Config as cms

tpSelectorByGenDefault = cms.EDProducer('TrackingParticleSelectorByGen',
  trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
  genParticles = cms.InputTag('genParticles'),
  select = cms.required.vstring,
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

digiSimLinkPrunerDefault = cms.EDProducer('DigiSimLinkPruner',
  trackingParticles = cms.required.InputTag,
  pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
  stripSimLinkSrc = cms.optional.InputTag,
  phase2OTSimLinkSrc = cms.optional.InputTag,
  mightGet = cms.optional.untracked.vstring
)

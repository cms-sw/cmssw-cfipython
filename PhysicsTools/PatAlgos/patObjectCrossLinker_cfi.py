import FWCore.ParameterSet.Config as cms

patObjectCrossLinker = cms.EDProducer('PATObjectCrossLinker',
  jets = cms.required.InputTag,
  muons = cms.required.InputTag,
  electrons = cms.required.InputTag,
  photons = cms.required.InputTag,
  taus = cms.required.InputTag,
  lowPtElectrons = cms.InputTag(''),
  boostedTaus = cms.InputTag(''),
  vertices = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)

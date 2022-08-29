import FWCore.ParameterSet.Config as cms

genJetConstituentSelector = cms.EDProducer('GenJetConstituentSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

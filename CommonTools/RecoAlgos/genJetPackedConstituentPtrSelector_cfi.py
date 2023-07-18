import FWCore.ParameterSet.Config as cms

genJetPackedConstituentPtrSelector = cms.EDProducer('GenJetPackedConstituentPtrSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

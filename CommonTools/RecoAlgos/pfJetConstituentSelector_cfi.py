import FWCore.ParameterSet.Config as cms

pfJetConstituentSelector = cms.EDProducer('PFJetConstituentSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

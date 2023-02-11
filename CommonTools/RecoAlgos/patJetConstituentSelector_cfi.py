import FWCore.ParameterSet.Config as cms

patJetConstituentSelector = cms.EDProducer('PatJetConstituentSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

patJetConstituentPtrSelector = cms.EDProducer('PatJetConstituentPtrSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

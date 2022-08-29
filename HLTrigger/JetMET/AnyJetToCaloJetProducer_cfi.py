import FWCore.ParameterSet.Config as cms

AnyJetToCaloJetProducer = cms.EDProducer('AnyJetToCaloJetProducer',
  Source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)

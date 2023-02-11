import FWCore.ParameterSet.Config as cms

JetRegressionVarProducer = cms.EDProducer('JetRegressionVarProducer',
  src = cms.required.InputTag,
  pvsrc = cms.required.InputTag,
  svsrc = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

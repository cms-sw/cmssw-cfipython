import FWCore.ParameterSet.Config as cms

ElectronJetVarProducer = cms.EDProducer('ElectronJetVarProducer',
  srcJet = cms.required.InputTag,
  srcLep = cms.required.InputTag,
  srcVtx = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

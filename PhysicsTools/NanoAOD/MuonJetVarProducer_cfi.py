import FWCore.ParameterSet.Config as cms

MuonJetVarProducer = cms.EDProducer('MuonJetVarProducer',
  srcJet = cms.required.InputTag,
  srcLep = cms.required.InputTag,
  srcVtx = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

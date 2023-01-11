import FWCore.ParameterSet.Config as cms

triggerObjectTableProducer = cms.EDProducer('TriggerObjectTableProducer',
  name = cms.required.string,
  src = cms.required.InputTag,
  l1EG = cms.required.InputTag,
  l1Sum = cms.required.InputTag,
  l1Jet = cms.required.InputTag,
  l1Muon = cms.required.InputTag,
  l1Tau = cms.required.InputTag,
  selections = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

l1tStage2uGMTInputBxDistributions = cms.EDProducer('L1TStage2uGMTInputBxDistributions',
  muonProducer = cms.required.InputTag,
  bmtfProducer = cms.required.InputTag,
  omtfProducer = cms.required.InputTag,
  emtfProducer = cms.required.InputTag,
  muonShowerProducer = cms.required.InputTag,
  emtfShowerProducer = cms.required.InputTag,
  monitorDir = cms.untracked.string(''),
  emulator = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False),
  hadronicShowers = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)

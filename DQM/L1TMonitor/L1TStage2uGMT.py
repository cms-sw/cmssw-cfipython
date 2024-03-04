import FWCore.ParameterSet.Config as cms

def L1TStage2uGMT(**kwargs):
  mod = cms.EDProducer('L1TStage2uGMT',
    muonProducer = cms.required.InputTag,
    bmtfProducer = cms.required.InputTag,
    omtfProducer = cms.required.InputTag,
    emtfProducer = cms.required.InputTag,
    muonShowerProducer = cms.required.InputTag,
    emtfShowerProducer = cms.required.InputTag,
    monitorDir = cms.untracked.string(''),
    emulator = cms.untracked.bool(False),
    verbose = cms.untracked.bool(False),
    displacedQuantities = cms.untracked.bool(False),
    hadronicShowers = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

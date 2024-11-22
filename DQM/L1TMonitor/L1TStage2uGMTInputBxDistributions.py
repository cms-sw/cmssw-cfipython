import FWCore.ParameterSet.Config as cms

def L1TStage2uGMTInputBxDistributions(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2uGMTInputBxDistributions',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

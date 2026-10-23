import FWCore.ParameterSet.Config as cms

def L1TStage2uGMTMuon(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2uGMTMuon',
    muonProducer = cms.required.InputTag,
    monitorDir = cms.untracked.string(''),
    titlePrefix = cms.untracked.string(''),
    verbose = cms.untracked.bool(False),
    makeMuonAtVtxPlots = cms.untracked.bool(False),
    displacedQuantities = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

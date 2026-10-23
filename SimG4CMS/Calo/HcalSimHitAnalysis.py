import FWCore.ParameterSet.Config as cms

def HcalSimHitAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSimHitAnalysis',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    HitCollection = cms.untracked.string('HcalHits'),
    Verbose = cms.untracked.bool(False),
    TestNumber = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

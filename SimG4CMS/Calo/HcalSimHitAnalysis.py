import FWCore.ParameterSet.Config as cms

def HcalSimHitAnalysis(**kwargs):
  mod = cms.EDAnalyzer('HcalSimHitAnalysis',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    HitCollection = cms.untracked.string('HcalHits'),
    Verbose = cms.untracked.bool(False),
    TestNumber = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

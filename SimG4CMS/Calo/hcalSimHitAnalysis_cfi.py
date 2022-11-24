import FWCore.ParameterSet.Config as cms

hcalSimHitAnalysis = cms.EDAnalyzer('HcalSimHitAnalysis',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  HitCollection = cms.untracked.string('HcalHits'),
  Verbose = cms.untracked.bool(False),
  TestNumber = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

HFPMTHitAnalyzer = cms.EDAnalyzer('HFPMTHitAnalyzer',
  SourceLabel = cms.untracked.string('generatorSmeared'),
  ModuleLabel = cms.untracked.string('g4SimHits'),
  HitCollection = cms.untracked.string('HcalHits'),
  mightGet = cms.optional.untracked.vstring
)

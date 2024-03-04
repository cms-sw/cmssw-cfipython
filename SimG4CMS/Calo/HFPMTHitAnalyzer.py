import FWCore.ParameterSet.Config as cms

def HFPMTHitAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HFPMTHitAnalyzer',
    SourceLabel = cms.untracked.string('generatorSmeared'),
    ModuleLabel = cms.untracked.string('g4SimHits'),
    HitCollection = cms.untracked.string('HcalHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HFPMTHitAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HFPMTHitAnalyzer',
    SourceLabel = cms.untracked.string('generatorSmeared'),
    ModuleLabel = cms.untracked.string('g4SimHits'),
    HitCollection = cms.untracked.string('HcalHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

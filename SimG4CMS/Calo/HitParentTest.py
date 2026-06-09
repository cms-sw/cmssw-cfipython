import FWCore.ParameterSet.Config as cms

def HitParentTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HitParentTest',
    SourceLabel = cms.untracked.string('generatorSmeared'),
    ModuleLabel = cms.untracked.string('g4SimHits'),
    EBCollection = cms.untracked.string('EcalHitsEB'),
    EECollection = cms.untracked.string('EcalHitsEE'),
    ESCollection = cms.untracked.string('EcalHitsES'),
    HCCollection = cms.untracked.string('HcalHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

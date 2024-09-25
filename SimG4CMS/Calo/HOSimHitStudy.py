import FWCore.ParameterSet.Config as cms

def HOSimHitStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('HOSimHitStudy',
    SourceLabel = cms.untracked.string('generatorSmeared'),
    ModuleLabel = cms.untracked.string('g4SimHits'),
    HitCollection = cms.untracked.vstring(
      'EcalHitsEB',
      'HcalHits'
    ),
    MaxEnergy = cms.untracked.double(50),
    ScaleEB = cms.untracked.double(1.02),
    ScaleHB = cms.untracked.double(104.4),
    ScaleHO = cms.untracked.double(2.33),
    TimeCut = cms.untracked.double(100),
    PrintExcessEnergy = cms.untracked.bool(True),
    TestNumbering = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

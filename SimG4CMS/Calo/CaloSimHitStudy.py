import FWCore.ParameterSet.Config as cms

def CaloSimHitStudy(**kwargs):
  mod = cms.EDAnalyzer('CaloSimHitStudy',
    SourceLabel = cms.untracked.string('generatorSmeared'),
    ModuleLabel = cms.untracked.string('g4SimHits'),
    CaloCollection = cms.untracked.vstring(
      'EcalHitsEB',
      'EcalHitsEE',
      'EcalHitsES',
      'HcalHits'
    ),
    MaxEnergy = cms.untracked.double(200),
    TimeCut = cms.untracked.double(100),
    MIPCut = cms.untracked.double(0.7),
    StoreRL = cms.untracked.bool(False),
    TestNumbering = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

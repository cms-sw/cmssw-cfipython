import FWCore.ParameterSet.Config as cms

def ZDCSimHitStudy(**kwargs):
  mod = cms.EDAnalyzer('ZDCSimHitStudy',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('ZDCHITS'),
    MaxEnergy = cms.double(50),
    TimeCut = cms.double(2000),
    Verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ZDCSimHitStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('ZDCSimHitStudy',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('ZDCHITS'),
    MaxEnergy = cms.double(50),
    TimeCut = cms.double(2000),
    Verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

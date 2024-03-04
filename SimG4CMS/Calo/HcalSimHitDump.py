import FWCore.ParameterSet.Config as cms

def HcalSimHitDump(**kwargs):
  mod = cms.EDAnalyzer('HcalSimHitDump',
    ModuleLabel = cms.string('g4SimHits'),
    HCCollection = cms.string('HcalHits'),
    MaxEvent = cms.int32(10),
    TestNumber = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

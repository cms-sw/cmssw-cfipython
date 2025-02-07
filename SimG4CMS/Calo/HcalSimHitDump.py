import FWCore.ParameterSet.Config as cms

def HcalSimHitDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSimHitDump',
    ModuleLabel = cms.string('g4SimHits'),
    HCCollection = cms.string('HcalHits'),
    MaxEvent = cms.int32(10),
    TestNumber = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def HcalTestSimHitID(**kwargs):
  mod = cms.EDAnalyzer('HcalTestSimHitID',
    moduleLabel = cms.untracked.string('g4SimHits'),
    hcCollection = cms.untracked.string('HcalHits'),
    testNumbering = cms.untracked.bool(False),
    dumpHits = cms.untracked.bool(False),
    maxEvent = cms.untracked.int32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HcalSimHitCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSimHitCheck',
    moduleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('HcalHits'),
    outputFile = cms.string('hcHit.root'),
    Verbose = cms.int32(0),
    TestNumber = cms.bool(True),
    hep17 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

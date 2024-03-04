import FWCore.ParameterSet.Config as cms

def HcalSimHitCheck(**kwargs):
  mod = cms.EDAnalyzer('HcalSimHitCheck',
    moduleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('HcalHits'),
    outputFile = cms.string('hcHit.root'),
    Verbose = cms.int32(0),
    TestNumber = cms.bool(True),
    hep17 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

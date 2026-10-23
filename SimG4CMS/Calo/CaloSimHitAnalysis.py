import FWCore.ParameterSet.Config as cms

def CaloSimHitAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloSimHitAnalysis',
    moduleLabel = cms.untracked.string('g4SimHits'),
    hitCollection = cms.vstring(
      'EcalHitsEB1',
      'EcalHitsEE1',
      'HcalHits1'
    ),
    timeSliceUnit = cms.vdouble(
      1,
      1,
      1
    ),
    maxEnergy = cms.untracked.double(250),
    maxTime = cms.untracked.double(1000),
    timeCut = cms.untracked.double(100),
    timeScale = cms.untracked.double(1),
    timeThreshold = cms.untracked.double(15),
    testNumbering = cms.untracked.bool(False),
    passiveHits = cms.untracked.bool(False),
    detNames = cms.untracked.vstring(
      'PixelBarrel',
      'PixelForward',
      'TIB',
      'TID',
      'TOB',
      'TEC'
    ),
    allStep = cms.untracked.int32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

caloSimHitAnalysis = cms.EDAnalyzer('CaloSimHitAnalysis',
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
  testNumbering = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)

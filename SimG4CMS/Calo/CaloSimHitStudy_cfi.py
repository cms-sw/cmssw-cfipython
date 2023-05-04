import FWCore.ParameterSet.Config as cms

CaloSimHitStudy = cms.EDAnalyzer('CaloSimHitStudy',
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

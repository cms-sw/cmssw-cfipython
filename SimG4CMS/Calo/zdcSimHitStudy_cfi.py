import FWCore.ParameterSet.Config as cms

zdcSimHitStudy = cms.EDAnalyzer('ZDCSimHitStudy',
  ModuleLabel = cms.string('g4SimHits'),
  HitCollection = cms.string('ZDCHITS'),
  MaxEnergy = cms.double(50),
  TimeCut = cms.double(2000),
  Verbose = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

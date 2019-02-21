import FWCore.ParameterSet.Config as cms

EcalSimHitStudy = cms.EDAnalyzer('EcalSimHitStudy',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  EBCollection = cms.untracked.string('EcalHitsEB'),
  EECollection = cms.untracked.string('EcalHitsEE'),
  SourceLabel = cms.untracked.string('VtxSmeared'),
  MaxEnergy = cms.untracked.double(200),
  TimeCut = cms.untracked.double(100),
  SelectX = cms.untracked.int32(-1)
)

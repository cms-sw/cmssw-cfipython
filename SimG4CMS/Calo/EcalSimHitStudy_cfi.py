import FWCore.ParameterSet.Config as cms

EcalSimHitStudy = cms.EDAnalyzer('EcalSimHitStudy',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  CaloCollection = cms.untracked.vstring(),
  SourceLabel = cms.untracked.string('VtxSmeared'),
  MaxEnergy = cms.untracked.double(200),
  TimeCut = cms.untracked.double(100),
  SelectX = cms.untracked.int32(-1),
  mightGet = cms.optional.untracked.vstring
)

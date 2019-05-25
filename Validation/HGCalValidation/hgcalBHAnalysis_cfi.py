import FWCore.ParameterSet.Config as cms

hgcalBHAnalysis = cms.EDAnalyzer('HGCalBHValidation',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  HitCollection = cms.untracked.string('HcalHits'),
  DigiCollection = cms.untracked.InputTag('hgcalDigis', 'HEback'),
  Sample = cms.untracked.int32(5),
  GeometryType = cms.untracked.int32(0),
  Threshold = cms.untracked.double(15),
  ifHCAL = cms.untracked.bool(False)
)

import FWCore.ParameterSet.Config as cms

hgcalBHAnalysis = cms.EDAnalyzer('HGCalBHValidation',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  HitCollection = cms.untracked.string('HGCHitsHEback'),
  DigiCollection = cms.untracked.InputTag('hgcalDigis', 'HEback'),
  Sample = cms.untracked.int32(5),
  GeometryType = cms.untracked.int32(1),
  Threshold = cms.untracked.double(15),
  ifHCAL = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)

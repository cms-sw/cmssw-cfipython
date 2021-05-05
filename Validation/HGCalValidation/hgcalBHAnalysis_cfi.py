import FWCore.ParameterSet.Config as cms

hgcalBHAnalysis = cms.EDAnalyzer('HGCalBHValidation',
  ModuleLabel = cms.string('g4SimHits'),
  HitCollection = cms.string('HGCHitsHEback'),
  DigiCollection = cms.InputTag('simHGCalUnsuppressedDigis', 'HEback'),
  Sample = cms.int32(5),
  Threshold = cms.double(15),
  mightGet = cms.optional.untracked.vstring
)

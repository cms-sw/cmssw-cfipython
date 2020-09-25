import FWCore.ParameterSet.Config as cms

hgcalSiliconAnalysisEE = cms.EDAnalyzer('HGCalSiliconValidation',
  ModuleLabel = cms.untracked.string('g4SimHits'),
  detectorName = cms.untracked.string('HGCalEESensitive'),
  HitCollection = cms.untracked.string('HGCHitsEE'),
  DigiCollection = cms.untracked.InputTag('simHGCalUnsuppressedDigis', 'EE'),
  Sample = cms.untracked.int32(5),
  mightGet = cms.optional.untracked.vstring
)

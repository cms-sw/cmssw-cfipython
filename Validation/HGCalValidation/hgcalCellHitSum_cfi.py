import FWCore.ParameterSet.Config as cms

hgcalCellHitSum = cms.EDAnalyzer('HGCalCellHitSum',
  simtrack = cms.InputTag('g4SimHits'),
  simhits = cms.InputTag('g4SimHits', 'HGCHitsEE'),
  detector = cms.string('HGCalEESensitive'),
  geometryFileName = cms.FileInPath('Validation/HGCalValidation/data/wafer_v17.csv'),
  mightGet = cms.optional.untracked.vstring
)

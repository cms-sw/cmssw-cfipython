import FWCore.ParameterSet.Config as cms

def HGCalCellHitSum(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalCellHitSum',
    simtrack = cms.InputTag('g4SimHits'),
    simhits = cms.InputTag('g4SimHits', 'HGCHitsEE'),
    detector = cms.string('HGCalEESensitive'),
    geometryFileName = cms.FileInPath('Validation/HGCalValidation/data/wafer_v17.csv'),
    layerList = cms.string('1'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

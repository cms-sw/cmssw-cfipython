import FWCore.ParameterSet.Config as cms

def HGCalCellHitSum(**kwargs):
  mod = cms.EDAnalyzer('HGCalCellHitSum',
    simtrack = cms.InputTag('g4SimHits'),
    simhits = cms.InputTag('g4SimHits', 'HGCHitsEE'),
    detector = cms.string('HGCalEESensitive'),
    geometryFileName = cms.FileInPath('Validation/HGCalValidation/data/wafer_v17.csv'),
    layerList = cms.string('1'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

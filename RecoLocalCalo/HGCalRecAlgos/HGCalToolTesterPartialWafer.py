import FWCore.ParameterSet.Config as cms

def HGCalToolTesterPartialWafer(**kwargs):
  mod = cms.EDAnalyzer('HGCalToolTesterPartialWafer',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

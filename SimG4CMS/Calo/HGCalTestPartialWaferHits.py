import FWCore.ParameterSet.Config as cms

def HGCalTestPartialWaferHits(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestPartialWaferHits',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    missingFile = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

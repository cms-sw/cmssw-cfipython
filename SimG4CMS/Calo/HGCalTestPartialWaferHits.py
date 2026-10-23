import FWCore.ParameterSet.Config as cms

def HGCalTestPartialWaferHits(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestPartialWaferHits',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    missingFile = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

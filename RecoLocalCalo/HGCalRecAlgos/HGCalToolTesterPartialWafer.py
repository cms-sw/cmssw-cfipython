import FWCore.ParameterSet.Config as cms

def HGCalToolTesterPartialWafer(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalToolTesterPartialWafer',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

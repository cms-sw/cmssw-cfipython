import FWCore.ParameterSet.Config as cms

def HGcalHitCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGcalHitCheck',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    nameDevice = cms.string('HGCal EE'),
    tag = cms.string('DDD'),
    layers = cms.int32(26),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

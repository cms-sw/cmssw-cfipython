import FWCore.ParameterSet.Config as cms

def HGcalHitIdCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGcalHitIdCheck',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsEE'),
    nameSense = cms.string('HGCalEESensitive'),
    nameDevice = cms.string('HGCal EE'),
    Verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

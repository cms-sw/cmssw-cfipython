import FWCore.ParameterSet.Config as cms

def HGCalTestScintHits(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestScintHits',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsHEback'),
    nameSense = cms.string('HGCalHEScintillatorSensitive'),
    tileFileName = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

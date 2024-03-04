import FWCore.ParameterSet.Config as cms

def HGCalTestScintHits(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestScintHits',
    moduleLabel = cms.string('g4SimHits'),
    caloHitSource = cms.string('HGCHitsHEback'),
    nameSense = cms.string('HGCalHEScintillatorSensitive'),
    tileFileName = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

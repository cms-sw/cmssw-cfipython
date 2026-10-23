import FWCore.ParameterSet.Config as cms

def HGCalSiliconValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalSiliconValidation',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    detectorName = cms.untracked.string('HGCalEESensitive'),
    HitCollection = cms.untracked.string('HGCHitsEE'),
    DigiCollection = cms.untracked.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    Sample = cms.untracked.int32(5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

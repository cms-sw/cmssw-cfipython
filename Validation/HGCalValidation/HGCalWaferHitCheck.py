import FWCore.ParameterSet.Config as cms

def HGCalWaferHitCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferHitCheck',
    detectorName = cms.string('HGCalEESensitive'),
    caloHitSource = cms.string('HGCHitsEE'),
    source = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    inputType = cms.int32(1),
    verbosity = cms.untracked.int32(0),
    ifNose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

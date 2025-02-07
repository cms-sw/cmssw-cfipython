import FWCore.ParameterSet.Config as cms

def HGCalTestPartialWaferRecHits(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestPartialWaferRecHits',
    detectorName = cms.string('HGCalEESensitive'),
    missingFile = cms.string(''),
    source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

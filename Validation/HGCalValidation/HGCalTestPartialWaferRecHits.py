import FWCore.ParameterSet.Config as cms

def HGCalTestPartialWaferRecHits(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestPartialWaferRecHits',
    detectorName = cms.string('HGCalEESensitive'),
    missingFile = cms.string(''),
    source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def MkFitEventOfHitsProducer(**kwargs):
  mod = cms.EDProducer('MkFitEventOfHitsProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    pixelHits = cms.InputTag('mkFitSiPixelHits'),
    stripHits = cms.InputTag('mkFitSiStripHits'),
    usePixelQualityDB = cms.bool(True),
    useStripStripQualityDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

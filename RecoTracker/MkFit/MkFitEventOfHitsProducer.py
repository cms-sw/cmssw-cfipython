import FWCore.ParameterSet.Config as cms

def MkFitEventOfHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('MkFitEventOfHitsProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    pixelHits = cms.InputTag('mkFitSiPixelHits'),
    stripHits = cms.InputTag('mkFitSiStripHits'),
    usePixelQualityDB = cms.bool(True),
    useStripStripQualityDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

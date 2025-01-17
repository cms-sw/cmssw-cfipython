import FWCore.ParameterSet.Config as cms

def MkFitSiPixelHitConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitSiPixelHitConverter',
    hits = cms.InputTag('siPixelRecHits'),
    clusters = cms.InputTag('siPixelClusters'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

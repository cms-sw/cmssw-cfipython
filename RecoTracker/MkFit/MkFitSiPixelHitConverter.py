import FWCore.ParameterSet.Config as cms

def MkFitSiPixelHitConverter(**kwargs):
  mod = cms.EDProducer('MkFitSiPixelHitConverter',
    hits = cms.InputTag('siPixelRecHits'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

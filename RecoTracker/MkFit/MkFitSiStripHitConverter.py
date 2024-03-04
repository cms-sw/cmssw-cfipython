import FWCore.ParameterSet.Config as cms

def MkFitSiStripHitConverter(**kwargs):
  mod = cms.EDProducer('MkFitSiStripHitConverter',
    rphiHits = cms.InputTag('siStripMatchedRecHits', 'rphiRecHit'),
    stereoHits = cms.InputTag('siStripMatchedRecHits', 'stereoRecHit'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    minGoodStripCharge = cms.PSet(
      value = cms.required.double
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

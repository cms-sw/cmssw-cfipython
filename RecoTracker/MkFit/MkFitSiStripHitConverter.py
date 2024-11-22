import FWCore.ParameterSet.Config as cms

def MkFitSiStripHitConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitSiStripHitConverter',
    rphiHits = cms.InputTag('siStripMatchedRecHits', 'rphiRecHit'),
    stereoHits = cms.InputTag('siStripMatchedRecHits', 'stereoRecHit'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    minGoodStripCharge = cms.PSet(
      value = cms.required.double
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

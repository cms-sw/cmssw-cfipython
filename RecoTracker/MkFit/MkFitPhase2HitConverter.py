import FWCore.ParameterSet.Config as cms

def MkFitPhase2HitConverter(**kwargs):
  mod = cms.EDProducer('MkFitPhase2HitConverter',
    siPhase2Hits = cms.InputTag('siPhase2RecHits'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

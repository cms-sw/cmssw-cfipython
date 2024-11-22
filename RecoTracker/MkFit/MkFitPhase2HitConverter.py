import FWCore.ParameterSet.Config as cms

def MkFitPhase2HitConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitPhase2HitConverter',
    siPhase2Hits = cms.InputTag('siPhase2RecHits'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

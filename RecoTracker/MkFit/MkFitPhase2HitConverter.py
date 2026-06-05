import FWCore.ParameterSet.Config as cms

def MkFitPhase2HitConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitPhase2HitConverter',
    hits = cms.InputTag('siPhase2RecHits'),
    clusters = cms.InputTag('siPhase2Clusters'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def LSTPhase2OTHitsInputProducer(*args, **kwargs):
  mod = cms.EDProducer('LSTPhase2OTHitsInputProducer',
    phase2OTRecHits = cms.InputTag('siPhase2RecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

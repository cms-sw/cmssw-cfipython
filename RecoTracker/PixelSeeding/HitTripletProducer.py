import FWCore.ParameterSet.Config as cms

def HitTripletProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('HitTripletProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

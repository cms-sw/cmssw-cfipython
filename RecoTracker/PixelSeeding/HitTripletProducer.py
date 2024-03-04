import FWCore.ParameterSet.Config as cms

def HitTripletProducer(**kwargs):
  mod = cms.EDAnalyzer('HitTripletProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

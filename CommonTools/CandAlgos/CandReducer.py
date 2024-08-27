import FWCore.ParameterSet.Config as cms

def CandReducer(**kwargs):
  mod = cms.EDProducer('CandReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

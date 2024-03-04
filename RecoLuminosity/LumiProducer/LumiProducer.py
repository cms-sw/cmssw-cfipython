import FWCore.ParameterSet.Config as cms

def LumiProducer(**kwargs):
  mod = cms.EDProducer('LumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

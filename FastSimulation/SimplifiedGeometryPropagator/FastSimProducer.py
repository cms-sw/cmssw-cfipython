import FWCore.ParameterSet.Config as cms

def FastSimProducer(**kwargs):
  mod = cms.EDProducer('FastSimProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

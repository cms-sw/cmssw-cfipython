import FWCore.ParameterSet.Config as cms

def L1RCTInputProducer(**kwargs):
  mod = cms.EDProducer('L1RCTInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

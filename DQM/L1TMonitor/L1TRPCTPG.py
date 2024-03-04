import FWCore.ParameterSet.Config as cms

def L1TRPCTPG(**kwargs):
  mod = cms.EDProducer('L1TRPCTPG',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

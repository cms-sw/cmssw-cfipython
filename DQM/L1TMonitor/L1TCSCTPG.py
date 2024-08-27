import FWCore.ParameterSet.Config as cms

def L1TCSCTPG(**kwargs):
  mod = cms.EDProducer('L1TCSCTPG',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

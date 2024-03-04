import FWCore.ParameterSet.Config as cms

def L1TdeCSCTPG(**kwargs):
  mod = cms.EDProducer('L1TdeCSCTPG',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

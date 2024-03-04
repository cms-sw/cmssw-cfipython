import FWCore.ParameterSet.Config as cms

def L1TdeCSCTF(**kwargs):
  mod = cms.EDProducer('L1TdeCSCTF',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

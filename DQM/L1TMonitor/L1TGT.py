import FWCore.ParameterSet.Config as cms

def L1TGT(**kwargs):
  mod = cms.EDProducer('L1TGT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

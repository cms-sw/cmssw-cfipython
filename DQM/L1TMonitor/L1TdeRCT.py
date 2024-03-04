import FWCore.ParameterSet.Config as cms

def L1TdeRCT(**kwargs):
  mod = cms.EDProducer('L1TdeRCT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

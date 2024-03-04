import FWCore.ParameterSet.Config as cms

def L1GtHwValidation(**kwargs):
  mod = cms.EDProducer('L1GtHwValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

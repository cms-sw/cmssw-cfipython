import FWCore.ParameterSet.Config as cms

def NearbyCandCountComputer(**kwargs):
  mod = cms.EDProducer('NearbyCandCountComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

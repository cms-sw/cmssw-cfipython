import FWCore.ParameterSet.Config as cms

def NearbyCandCountComputer(*args, **kwargs):
  mod = cms.EDProducer('NearbyCandCountComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

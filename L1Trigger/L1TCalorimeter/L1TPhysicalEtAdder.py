import FWCore.ParameterSet.Config as cms

def L1TPhysicalEtAdder(*args, **kwargs):
  mod = cms.EDProducer('L1TPhysicalEtAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

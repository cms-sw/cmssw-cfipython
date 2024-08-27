import FWCore.ParameterSet.Config as cms

def L1TPhysicalEtAdder(**kwargs):
  mod = cms.EDProducer('L1TPhysicalEtAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

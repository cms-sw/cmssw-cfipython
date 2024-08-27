import FWCore.ParameterSet.Config as cms

def DeltaRNearestPhotonComputer(**kwargs):
  mod = cms.EDProducer('DeltaRNearestPhotonComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

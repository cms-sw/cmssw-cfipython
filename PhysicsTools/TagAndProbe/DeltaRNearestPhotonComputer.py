import FWCore.ParameterSet.Config as cms

def DeltaRNearestPhotonComputer(*args, **kwargs):
  mod = cms.EDProducer('DeltaRNearestPhotonComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

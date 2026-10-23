import FWCore.ParameterSet.Config as cms

def DeltaRNearestGsfElectronComputer(*args, **kwargs):
  mod = cms.EDProducer('DeltaRNearestGsfElectronComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

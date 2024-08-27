import FWCore.ParameterSet.Config as cms

def DeltaRNearestGsfElectronComputer(**kwargs):
  mod = cms.EDProducer('DeltaRNearestGsfElectronComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

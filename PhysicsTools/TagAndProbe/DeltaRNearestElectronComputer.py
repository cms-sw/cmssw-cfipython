import FWCore.ParameterSet.Config as cms

def DeltaRNearestElectronComputer(**kwargs):
  mod = cms.EDProducer('DeltaRNearestElectronComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

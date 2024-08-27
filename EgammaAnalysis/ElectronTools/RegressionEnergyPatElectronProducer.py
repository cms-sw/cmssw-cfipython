import FWCore.ParameterSet.Config as cms

def RegressionEnergyPatElectronProducer(**kwargs):
  mod = cms.EDProducer('RegressionEnergyPatElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

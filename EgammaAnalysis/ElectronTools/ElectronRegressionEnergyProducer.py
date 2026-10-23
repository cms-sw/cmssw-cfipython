import FWCore.ParameterSet.Config as cms

def ElectronRegressionEnergyProducer(*args, **kwargs):
  mod = cms.EDFilter('ElectronRegressionEnergyProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

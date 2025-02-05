import FWCore.ParameterSet.Config as cms

def ElectronEfficiencyPlotter(*args, **kwargs):
  mod = cms.EDProducer('ElectronEfficiencyPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

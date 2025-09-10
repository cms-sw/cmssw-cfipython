import FWCore.ParameterSet.Config as cms

def ElectronRecalibSuperClusterAssociator(*args, **kwargs):
  mod = cms.EDProducer('ElectronRecalibSuperClusterAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

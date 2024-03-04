import FWCore.ParameterSet.Config as cms

def ElectronRecalibSuperClusterAssociator(**kwargs):
  mod = cms.EDProducer('ElectronRecalibSuperClusterAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

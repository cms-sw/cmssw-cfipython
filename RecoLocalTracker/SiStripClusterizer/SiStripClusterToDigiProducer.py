import FWCore.ParameterSet.Config as cms

def SiStripClusterToDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripClusterToDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

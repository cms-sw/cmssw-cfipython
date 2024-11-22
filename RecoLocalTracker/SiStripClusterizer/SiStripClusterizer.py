import FWCore.ParameterSet.Config as cms

def SiStripClusterizer(*args, **kwargs):
  mod = cms.EDProducer('SiStripClusterizer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SiStripClusterizer(**kwargs):
  mod = cms.EDProducer('SiStripClusterizer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

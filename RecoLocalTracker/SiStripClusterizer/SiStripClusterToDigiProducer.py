import FWCore.ParameterSet.Config as cms

def SiStripClusterToDigiProducer(**kwargs):
  mod = cms.EDProducer('SiStripClusterToDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

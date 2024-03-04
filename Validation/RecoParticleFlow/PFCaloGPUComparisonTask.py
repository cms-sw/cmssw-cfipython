import FWCore.ParameterSet.Config as cms

def PFCaloGPUComparisonTask(**kwargs):
  mod = cms.EDProducer('PFCaloGPUComparisonTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

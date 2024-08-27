import FWCore.ParameterSet.Config as cms

def GenMETExtractor(**kwargs):
  mod = cms.EDProducer('GenMETExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

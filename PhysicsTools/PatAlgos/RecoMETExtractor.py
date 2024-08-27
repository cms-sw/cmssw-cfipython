import FWCore.ParameterSet.Config as cms

def RecoMETExtractor(**kwargs):
  mod = cms.EDProducer('RecoMETExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

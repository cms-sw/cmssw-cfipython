import FWCore.ParameterSet.Config as cms

def DataMixingModule(**kwargs):
  mod = cms.EDProducer('DataMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def MixingModule(**kwargs):
  mod = cms.EDProducer('MixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PreMixingModule(**kwargs):
  mod = cms.EDProducer('PreMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

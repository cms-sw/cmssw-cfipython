import FWCore.ParameterSet.Config as cms

def HiMixingModule(**kwargs):
  mod = cms.EDProducer('HiMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

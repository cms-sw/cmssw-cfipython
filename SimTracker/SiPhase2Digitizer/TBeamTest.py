import FWCore.ParameterSet.Config as cms

def TBeamTest(**kwargs):
  mod = cms.EDProducer('TBeamTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

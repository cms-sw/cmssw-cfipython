import FWCore.ParameterSet.Config as cms

def RecHitCorrector(**kwargs):
  mod = cms.EDProducer('RecHitCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

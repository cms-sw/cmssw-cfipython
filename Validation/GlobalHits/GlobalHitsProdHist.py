import FWCore.ParameterSet.Config as cms

def GlobalHitsProdHist(**kwargs):
  mod = cms.EDProducer('GlobalHitsProdHist',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

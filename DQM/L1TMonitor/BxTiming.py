import FWCore.ParameterSet.Config as cms

def BxTiming(**kwargs):
  mod = cms.EDProducer('BxTiming',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TkConvValidator(**kwargs):
  mod = cms.EDProducer('TkConvValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

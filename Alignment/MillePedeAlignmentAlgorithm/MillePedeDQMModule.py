import FWCore.ParameterSet.Config as cms

def MillePedeDQMModule(**kwargs):
  mod = cms.EDProducer('MillePedeDQMModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

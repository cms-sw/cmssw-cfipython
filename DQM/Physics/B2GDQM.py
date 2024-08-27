import FWCore.ParameterSet.Config as cms

def B2GDQM(**kwargs):
  mod = cms.EDProducer('B2GDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

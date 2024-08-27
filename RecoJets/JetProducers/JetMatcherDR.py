import FWCore.ParameterSet.Config as cms

def JetMatcherDR(**kwargs):
  mod = cms.EDProducer('JetMatcherDR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

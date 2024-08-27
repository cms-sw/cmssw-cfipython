import FWCore.ParameterSet.Config as cms

def JetTesterPostProcessor(**kwargs):
  mod = cms.EDProducer('JetTesterPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

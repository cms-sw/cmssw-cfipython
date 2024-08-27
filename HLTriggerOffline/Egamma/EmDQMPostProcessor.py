import FWCore.ParameterSet.Config as cms

def EmDQMPostProcessor(**kwargs):
  mod = cms.EDProducer('EmDQMPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

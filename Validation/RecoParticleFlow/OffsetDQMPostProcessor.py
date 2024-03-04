import FWCore.ParameterSet.Config as cms

def OffsetDQMPostProcessor(**kwargs):
  mod = cms.EDProducer('OffsetDQMPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

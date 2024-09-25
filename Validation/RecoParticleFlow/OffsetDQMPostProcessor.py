import FWCore.ParameterSet.Config as cms

def OffsetDQMPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('OffsetDQMPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

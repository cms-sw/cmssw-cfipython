import FWCore.ParameterSet.Config as cms

def UMNioTask(*args, **kwargs):
  mod = cms.EDProducer('UMNioTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

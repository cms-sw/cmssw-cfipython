import FWCore.ParameterSet.Config as cms

def UMNioTask(**kwargs):
  mod = cms.EDProducer('UMNioTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

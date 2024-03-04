import FWCore.ParameterSet.Config as cms

def DTResolutionTest(**kwargs):
  mod = cms.EDProducer('DTResolutionTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

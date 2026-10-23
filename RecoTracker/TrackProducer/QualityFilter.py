import FWCore.ParameterSet.Config as cms

def QualityFilter(*args, **kwargs):
  mod = cms.EDProducer('QualityFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

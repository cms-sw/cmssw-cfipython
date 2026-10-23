import FWCore.ParameterSet.Config as cms

def TrajectoryCombiner(*args, **kwargs):
  mod = cms.EDProducer('TrajectoryCombiner',
    labels = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

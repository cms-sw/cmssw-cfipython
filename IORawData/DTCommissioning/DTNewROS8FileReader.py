import FWCore.ParameterSet.Config as cms

def DTNewROS8FileReader(*args, **kwargs):
  mod = cms.EDProducer('DTNewROS8FileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

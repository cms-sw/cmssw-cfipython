import FWCore.ParameterSet.Config as cms

def LaserAlignmentProducer(*args, **kwargs):
  mod = cms.EDProducer('LaserAlignmentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

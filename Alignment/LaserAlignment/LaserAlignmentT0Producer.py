import FWCore.ParameterSet.Config as cms

def LaserAlignmentT0Producer(*args, **kwargs):
  mod = cms.EDProducer('LaserAlignmentT0Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

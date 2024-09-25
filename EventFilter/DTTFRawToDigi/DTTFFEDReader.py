import FWCore.ParameterSet.Config as cms

def DTTFFEDReader(*args, **kwargs):
  mod = cms.EDProducer('DTTFFEDReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

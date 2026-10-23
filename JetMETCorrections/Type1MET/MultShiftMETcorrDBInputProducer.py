import FWCore.ParameterSet.Config as cms

def MultShiftMETcorrDBInputProducer(*args, **kwargs):
  mod = cms.EDProducer('MultShiftMETcorrDBInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SysShiftMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('SysShiftMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

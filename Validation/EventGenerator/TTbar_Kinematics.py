import FWCore.ParameterSet.Config as cms

def TTbar_Kinematics(*args, **kwargs):
  mod = cms.EDProducer('TTbar_Kinematics',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

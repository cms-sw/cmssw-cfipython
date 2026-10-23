import FWCore.ParameterSet.Config as cms

def V0ReBuilder(*args, **kwargs):
  mod = cms.EDProducer('V0ReBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

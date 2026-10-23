import FWCore.ParameterSet.Config as cms

def DQMHOAlCaRecoStream(*args, **kwargs):
  mod = cms.EDProducer('DQMHOAlCaRecoStream',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

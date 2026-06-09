import FWCore.ParameterSet.Config as cms

def SMPDQM(*args, **kwargs):
  mod = cms.EDProducer('SMPDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

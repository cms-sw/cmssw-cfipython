import FWCore.ParameterSet.Config as cms

def FSQDQM(*args, **kwargs):
  mod = cms.EDProducer('FSQDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

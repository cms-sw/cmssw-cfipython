import FWCore.ParameterSet.Config as cms

def RctRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('RctRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

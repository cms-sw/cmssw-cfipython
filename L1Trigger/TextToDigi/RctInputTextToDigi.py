import FWCore.ParameterSet.Config as cms

def RctInputTextToDigi(*args, **kwargs):
  mod = cms.EDProducer('RctInputTextToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

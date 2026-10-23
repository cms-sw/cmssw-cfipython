import FWCore.ParameterSet.Config as cms

def RctTextToRctDigi(*args, **kwargs):
  mod = cms.EDProducer('RctTextToRctDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

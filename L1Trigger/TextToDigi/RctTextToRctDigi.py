import FWCore.ParameterSet.Config as cms

def RctTextToRctDigi(**kwargs):
  mod = cms.EDProducer('RctTextToRctDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

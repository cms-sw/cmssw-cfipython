import FWCore.ParameterSet.Config as cms

def RctRawToDigi(**kwargs):
  mod = cms.EDProducer('RctRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

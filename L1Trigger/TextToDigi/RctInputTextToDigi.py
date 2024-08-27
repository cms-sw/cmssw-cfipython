import FWCore.ParameterSet.Config as cms

def RctInputTextToDigi(**kwargs):
  mod = cms.EDProducer('RctInputTextToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ScGMTRawToDigi(**kwargs):
  mod = cms.EDProducer('ScGMTRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

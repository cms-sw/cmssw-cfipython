import FWCore.ParameterSet.Config as cms

def ScBMTFRawToDigi(**kwargs):
  mod = cms.EDProducer('ScBMTFRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

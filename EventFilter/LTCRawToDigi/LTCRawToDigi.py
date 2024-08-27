import FWCore.ParameterSet.Config as cms

def LTCRawToDigi(**kwargs):
  mod = cms.EDProducer('LTCRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

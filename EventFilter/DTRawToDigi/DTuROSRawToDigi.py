import FWCore.ParameterSet.Config as cms

def DTuROSRawToDigi(**kwargs):
  mod = cms.EDProducer('DTuROSRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

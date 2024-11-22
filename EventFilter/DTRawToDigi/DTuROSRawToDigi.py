import FWCore.ParameterSet.Config as cms

def DTuROSRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('DTuROSRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

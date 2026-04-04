import FWCore.ParameterSet.Config as cms

def LTCRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('LTCRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

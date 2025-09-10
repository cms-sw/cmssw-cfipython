import FWCore.ParameterSet.Config as cms

def DTDigitizer(*args, **kwargs):
  mod = cms.EDProducer('DTDigitizer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

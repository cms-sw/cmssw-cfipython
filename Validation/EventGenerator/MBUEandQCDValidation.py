import FWCore.ParameterSet.Config as cms

def MBUEandQCDValidation(*args, **kwargs):
  mod = cms.EDProducer('MBUEandQCDValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

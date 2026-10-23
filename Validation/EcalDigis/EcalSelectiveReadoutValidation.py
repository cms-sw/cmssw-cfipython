import FWCore.ParameterSet.Config as cms

def EcalSelectiveReadoutValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalSelectiveReadoutValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

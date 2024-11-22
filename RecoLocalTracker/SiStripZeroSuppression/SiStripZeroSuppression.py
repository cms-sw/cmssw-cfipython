import FWCore.ParameterSet.Config as cms

def SiStripZeroSuppression(*args, **kwargs):
  mod = cms.EDProducer('SiStripZeroSuppression',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SiStripZeroSuppression(**kwargs):
  mod = cms.EDProducer('SiStripZeroSuppression',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

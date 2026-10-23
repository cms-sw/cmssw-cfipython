import FWCore.ParameterSet.Config as cms

def SiStripDigiValid(*args, **kwargs):
  mod = cms.EDProducer('SiStripDigiValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

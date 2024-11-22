import FWCore.ParameterSet.Config as cms

def SiStripRawToDigiModule(*args, **kwargs):
  mod = cms.EDProducer('SiStripRawToDigiModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

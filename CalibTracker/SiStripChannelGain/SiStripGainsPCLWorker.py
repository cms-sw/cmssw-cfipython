import FWCore.ParameterSet.Config as cms

def SiStripGainsPCLWorker(*args, **kwargs):
  mod = cms.EDProducer('SiStripGainsPCLWorker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

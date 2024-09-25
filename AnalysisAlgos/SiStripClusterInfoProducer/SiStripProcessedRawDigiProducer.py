import FWCore.ParameterSet.Config as cms

def SiStripProcessedRawDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripProcessedRawDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

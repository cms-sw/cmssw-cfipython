import FWCore.ParameterSet.Config as cms

def SiStripGainsPCLWorker(**kwargs):
  mod = cms.EDProducer('SiStripGainsPCLWorker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

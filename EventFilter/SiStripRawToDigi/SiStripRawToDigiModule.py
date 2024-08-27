import FWCore.ParameterSet.Config as cms

def SiStripRawToDigiModule(**kwargs):
  mod = cms.EDProducer('SiStripRawToDigiModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

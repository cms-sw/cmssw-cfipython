import FWCore.ParameterSet.Config as cms

def SiStripSpyDigiConverterModule(**kwargs):
  mod = cms.EDProducer('SiStripSpyDigiConverterModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

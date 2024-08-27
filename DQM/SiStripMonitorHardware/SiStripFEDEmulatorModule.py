import FWCore.ParameterSet.Config as cms

def SiStripFEDEmulatorModule(**kwargs):
  mod = cms.EDProducer('SiStripFEDEmulatorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

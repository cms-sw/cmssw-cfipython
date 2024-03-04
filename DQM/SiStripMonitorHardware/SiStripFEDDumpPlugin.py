import FWCore.ParameterSet.Config as cms

def SiStripFEDDumpPlugin(**kwargs):
  mod = cms.EDProducer('SiStripFEDDumpPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

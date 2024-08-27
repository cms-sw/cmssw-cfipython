import FWCore.ParameterSet.Config as cms

def SiStripPopConPedestalsDQM(**kwargs):
  mod = cms.EDProducer('SiStripPopConPedestalsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def SiStripPopConPedestalsDQM(*args, **kwargs):
  mod = cms.EDProducer('SiStripPopConPedestalsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

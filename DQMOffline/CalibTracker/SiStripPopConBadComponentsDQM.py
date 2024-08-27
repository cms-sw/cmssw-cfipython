import FWCore.ParameterSet.Config as cms

def SiStripPopConBadComponentsDQM(**kwargs):
  mod = cms.EDProducer('SiStripPopConBadComponentsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

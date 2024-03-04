import FWCore.ParameterSet.Config as cms

def SiStripPopConNoisesDQM(**kwargs):
  mod = cms.EDProducer('SiStripPopConNoisesDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

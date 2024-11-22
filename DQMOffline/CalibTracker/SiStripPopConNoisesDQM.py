import FWCore.ParameterSet.Config as cms

def SiStripPopConNoisesDQM(*args, **kwargs):
  mod = cms.EDProducer('SiStripPopConNoisesDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

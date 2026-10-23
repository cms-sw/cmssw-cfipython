import FWCore.ParameterSet.Config as cms

def SiStripPopConBadComponentsDQM(*args, **kwargs):
  mod = cms.EDProducer('SiStripPopConBadComponentsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

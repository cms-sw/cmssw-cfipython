import FWCore.ParameterSet.Config as cms

def SiStripFineDelayHit(**kwargs):
  mod = cms.EDProducer('SiStripFineDelayHit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

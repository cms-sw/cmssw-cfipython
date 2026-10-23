import FWCore.ParameterSet.Config as cms

def SiStripFineDelayHit(*args, **kwargs):
  mod = cms.EDProducer('SiStripFineDelayHit',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

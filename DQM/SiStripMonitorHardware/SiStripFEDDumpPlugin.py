import FWCore.ParameterSet.Config as cms

def SiStripFEDDumpPlugin(*args, **kwargs):
  mod = cms.EDProducer('SiStripFEDDumpPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

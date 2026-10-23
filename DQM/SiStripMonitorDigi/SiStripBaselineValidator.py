import FWCore.ParameterSet.Config as cms

def SiStripBaselineValidator(*args, **kwargs):
  mod = cms.EDProducer('SiStripBaselineValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ZDCDigiStudy(*args, **kwargs):
  mod = cms.EDProducer('ZDCDigiStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

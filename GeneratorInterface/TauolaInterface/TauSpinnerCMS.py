import FWCore.ParameterSet.Config as cms

def TauSpinnerCMS(*args, **kwargs):
  mod = cms.EDProducer('TauSpinnerCMS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

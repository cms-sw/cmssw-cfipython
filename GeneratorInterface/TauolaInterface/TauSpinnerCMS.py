import FWCore.ParameterSet.Config as cms

def TauSpinnerCMS(**kwargs):
  mod = cms.EDProducer('TauSpinnerCMS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TkLasBeamFitter(**kwargs):
  mod = cms.EDProducer('TkLasBeamFitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

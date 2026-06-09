import FWCore.ParameterSet.Config as cms

def OniaPhotonConversionProducer(*args, **kwargs):
  mod = cms.EDProducer('OniaPhotonConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

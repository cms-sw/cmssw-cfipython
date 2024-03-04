import FWCore.ParameterSet.Config as cms

def OniaPhotonConversionProducer(**kwargs):
  mod = cms.EDProducer('OniaPhotonConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

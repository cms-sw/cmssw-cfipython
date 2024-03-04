import FWCore.ParameterSet.Config as cms

def GEMCheckGeometry(**kwargs):
  mod = cms.EDProducer('GEMCheckGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PATHemisphereProducer(**kwargs):
  mod = cms.EDProducer('PATHemisphereProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ManyIntWhenRegisteredProducer(**kwargs):
  mod = cms.EDProducer('ManyIntWhenRegisteredProducer',
    src = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

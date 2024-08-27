import FWCore.ParameterSet.Config as cms

def CastorSimpleReconstructor(**kwargs):
  mod = cms.EDProducer('CastorSimpleReconstructor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def GsfVertexFitCompositeCandProducer(*args, **kwargs):
  mod = cms.EDProducer('GsfVertexFitCompositeCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

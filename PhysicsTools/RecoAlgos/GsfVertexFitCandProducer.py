import FWCore.ParameterSet.Config as cms

def GsfVertexFitCandProducer(*args, **kwargs):
  mod = cms.EDProducer('GsfVertexFitCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

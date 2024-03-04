import FWCore.ParameterSet.Config as cms

def HighestSumP4PrimaryVertexSelector(**kwargs):
  mod = cms.EDProducer('HighestSumP4PrimaryVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

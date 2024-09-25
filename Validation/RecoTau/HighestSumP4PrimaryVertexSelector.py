import FWCore.ParameterSet.Config as cms

def HighestSumP4PrimaryVertexSelector(*args, **kwargs):
  mod = cms.EDProducer('HighestSumP4PrimaryVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

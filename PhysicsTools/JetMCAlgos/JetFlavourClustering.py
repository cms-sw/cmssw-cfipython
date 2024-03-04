import FWCore.ParameterSet.Config as cms

def JetFlavourClustering(**kwargs):
  mod = cms.EDProducer('JetFlavourClustering',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

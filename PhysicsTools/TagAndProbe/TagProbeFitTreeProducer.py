import FWCore.ParameterSet.Config as cms

def TagProbeFitTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('TagProbeFitTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TagProbeFitTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('TagProbeFitTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

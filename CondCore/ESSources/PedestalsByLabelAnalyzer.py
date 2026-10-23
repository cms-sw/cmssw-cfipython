import FWCore.ParameterSet.Config as cms

def PedestalsByLabelAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PedestalsByLabelAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

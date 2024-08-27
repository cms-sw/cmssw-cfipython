import FWCore.ParameterSet.Config as cms

def PedestalsByLabelAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PedestalsByLabelAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

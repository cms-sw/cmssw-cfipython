import FWCore.ParameterSet.Config as cms

def SiPMNonlinearityAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiPMNonlinearityAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

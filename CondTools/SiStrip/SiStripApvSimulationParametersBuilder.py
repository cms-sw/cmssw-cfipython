import FWCore.ParameterSet.Config as cms

def SiStripApvSimulationParametersBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvSimulationParametersBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

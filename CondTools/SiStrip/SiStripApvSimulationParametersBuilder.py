import FWCore.ParameterSet.Config as cms

def SiStripApvSimulationParametersBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvSimulationParametersBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

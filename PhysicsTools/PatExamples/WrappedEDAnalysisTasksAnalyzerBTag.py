import FWCore.ParameterSet.Config as cms

def WrappedEDAnalysisTasksAnalyzerBTag(**kwargs):
  mod = cms.EDAnalyzer('WrappedEDAnalysisTasksAnalyzerBTag',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

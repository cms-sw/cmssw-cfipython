import FWCore.ParameterSet.Config as cms

def WrappedEDAnalysisTasksAnalyzerBTag(*args, **kwargs):
  mod = cms.EDAnalyzer('WrappedEDAnalysisTasksAnalyzerBTag',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def WrappedEDAnalysisTasksAnalyzerJEC(*args, **kwargs):
  mod = cms.EDAnalyzer('WrappedEDAnalysisTasksAnalyzerJEC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

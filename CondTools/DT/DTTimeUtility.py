import FWCore.ParameterSet.Config as cms

def DTTimeUtility(**kwargs):
  mod = cms.EDAnalyzer('DTTimeUtility',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
